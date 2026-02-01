import time


def get_transition_value(start_time, duration=5, start_val=-10, end_val=10):
    elapsed = time.time() - start_time

    # Calculate progress (0.0 to 1.0)
    progress = min(elapsed / duration, 1.0)

    # Linear mapping
    current_value = start_val + (end_val - start_val) * progress
    return current_value


# --- Usage Example ---
duration = 5
start = time.time()

print("Starting transition...")
while time.time() - start <= duration + 0.1:  # Small buffer to hit the final 10
    val = get_transition_value(start, duration)
    print(f"Current Value: {val:.2f}")
    time.sleep(0.5)  # Print every half second