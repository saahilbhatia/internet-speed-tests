import speedtest
import csv
import time

# Function to run speed tests
def run_speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000  # Convert to Mbps
    upload_speed = st.upload() / 1000000  # Convert to Mbps
    return download_speed, upload_speed

# Ask user for duration and frequency of speed tests
duration = int(input("Enter duration of speed test (in minutes): "))
frequency = int(input("Enter frequency of speed test (in minutes): "))

# Open CSV file to write results
with open("speed_test_results.csv", mode="w", newline='') as csv_file:
    fieldnames = ['Download Speed (Mbps)', 'Upload Speed (Mbps)']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write header row to CSV file
    writer.writeheader()

    # Run speed tests at specified frequency for specified duration
    num_tests = duration // frequency
    download_speeds = []
    upload_speeds = []
    for i in range(num_tests):
        print("Starting test number:", str(i+1))
        download_speed, upload_speed = run_speed_test()
        download_speeds.append(download_speed)
        upload_speeds.append(upload_speed)

        # Write speed test results to CSV file
        writer.writerow({'Download Speed (Mbps)': download_speed, 'Upload Speed (Mbps)': upload_speed})

        # Wait for specified frequency before running next test
        time.sleep(frequency * 60)

# Print minimum, maximum, and average speeds
print("Minimum download speed (Mbps):", min(download_speeds))
print("Maximum download speed (Mbps):", max(download_speeds))
print("Average download speed (Mbps):", sum(download_speeds) / len(download_speeds))
print("Minimum upload speed (Mbps):", min(upload_speeds))
print("Maximum upload speed (Mbps):", max(upload_speeds))
print("Average upload speed (Mbps):", sum(upload_speeds) / len(upload_speeds))
