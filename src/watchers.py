import os
import handle_data as hd
import re
import time
import threading
import shutil

def watch_for_inputs(week_number, base_dir = 'data', poll_interval = 5):
    """
    Poll raw/inputs.txt every `poll_interval` seconds.
    As soon as it appears (and hasn't been processed yet), process it and stop.
    """
    week = "week" + str(week_number)

    input_path  = os.path.join(base_dir, week, "raw", "inputs.txt")
    output_path = os.path.join(base_dir, week, "processed", "inputs.txt")

    raw_outputs_path = os.path.join(base_dir, week, "raw", "outputs.txt")
    processed_outputs_path = os.path.join(base_dir, week, "processed", "outputs.txt")
    
    if hd.is_already_processed(output_path):
        return
    
    print(f"[Weekly setup] --- Watching for {input_path}. Checking every {poll_interval}s.")

    while True:
        if os.path.exists(input_path):
            print(f"[Weekly setup] --- inputs.txt found: processing...")
            hd.process_raw(input_path, output_path)
            shutil.copy(raw_outputs_path, processed_outputs_path)
            print(f"[Weekly setup] --- Raw inputs have been processed.")
            print(f"[Weekly setup] --- Raw outputs have been processed.")
            break
        
        time.sleep(poll_interval)



def start_watcher(week_number, base_dir: str = "data", poll_interval: int = 5):
    """Run the watcher in a background thread so the notebook stays responsive."""
    thread = threading.Thread(
        target=watch_for_inputs,
        args=(week_number, base_dir, poll_interval),
        daemon=True
    )
    thread.start()
    return thread