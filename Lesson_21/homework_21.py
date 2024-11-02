from datetime import datetime


def analyze_heartbeat(log_file='hblog.txt', output_file='hb_test.log', key="Key TSTFEED0300|7E3E|0400"):
    with open(log_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Filtering rows with the desired key
    filtered_log = [line for line in lines if key in line]

    # Opening a file to record only WARNING and ERROR results
    with open(output_file, 'w', encoding='utf-8') as output:
        previous_timestamp = None

        for line in filtered_log:
            # Extract Timestamp
            time_pos = line.find("Timestamp ")
            if time_pos != -1:
                # Retrieve the timestamp and convert to datetime
                timestamp_str = line[time_pos + 10:time_pos + 18]

                try:
                    current_timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")
                except ValueError:
                    continue  # Skip the line if timestamp conversion fails

                # Calculate the absolute interval if there's a previous timestamp
                if previous_timestamp:
                    delta = abs((current_timestamp - previous_timestamp).total_seconds())

                    # Log only if the interval meets the specified conditions
                    if 31 < delta < 33:
                        output.write(f"WARNING: Heartbeat interval {delta} seconds at {timestamp_str}\n")
                    elif delta >= 33:
                        output.write(f"ERROR: Heartbeat interval {delta} seconds at {timestamp_str}\n")

                # Update the previous timestamp
                previous_timestamp = current_timestamp


analyze_heartbeat('hblog.txt', 'hb_test.log')
