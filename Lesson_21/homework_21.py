from datetime import datetime


def analyze_heartbeat(log_file='hblog.txt', output_file='hb_test.log', key="Key TSTFEED0300|7E3E|0400"):
    with open(log_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Filtering rows with the desired key
    filtered_log = [line for line in lines if key in line]

    # Opening a file to record analysis results
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(f"Найдено строк с ключом '{key}': {len(filtered_log)}\n")

        # Check: if there are no rows with the specified key, terminate execution
        if not filtered_log:
            output.write("Нет строк с указанным ключом.\n")
            return

        previous_timestamp = None

        for line in filtered_log:
            # Extract Timestamp
            time_pos = line.find("Timestamp ")
            if time_pos != -1:
                # Retrieving a timestamp and converting to a time object
                timestamp_str = line[time_pos + 10:time_pos + 18]
                output.write(f"Извлеченная временная метка: {timestamp_str}\n")

                try:
                    current_timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")
                    output.write(f"Объект времени: {current_timestamp}\n")
                except ValueError as e:
                    output.write(f"Ошибка преобразования временной метки: {e}\n")
                    continue

                # If a previous timestamp exists, calculate the difference
                if previous_timestamp:
                    delta = (current_timestamp - previous_timestamp).total_seconds()
                    output.write(f"Интервал между метками: {delta} секунд\n")

                    # Logging based on heartbeat interval
                    if 31 < delta < 33:
                        output.write(f"WARNING: Heartbeat interval {delta} seconds at {timestamp_str}\n")
                    elif delta >= 33:
                        output.write(f"ERROR: Heartbeat interval {delta} seconds at {timestamp_str}\n")

                # Update previous timestamp
                previous_timestamp = current_timestamp
            else:
                output.write("Временная метка не найдена в строке\n")


analyze_heartbeat('hblog.txt', 'hb_test.log')
