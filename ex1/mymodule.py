def handler(input: dict, context: object) -> dict:
    # Calculating auxiliary percentages
    byte_sum = input['net_io_counters_eth0-bytes_sent'] + input['net_io_counters_eth0-bytes_recv']
    memory_caching_content = input['virtual_memory-cached'] + input['virtual_memory-buffers']
    
    # Calculating CPU moving mean
    cpu_keys = [key for key in input.keys() if key.startswith("cpu_percent-")]
    
    # Check if env's been initialized
    context.env.update({f"cpu_percent-{i}": context.env.get(f"cpu_percent-{i}", 0) for i in range(len(cpu_keys))})
    
    moving_mean_dict = {
        f"avg-cpu{i}-60sec": context.env[f'cpu_percent-{i}'] + input[key] for i, key in enumerate(cpu_keys)    
    }
    context.env = moving_mean_dict
    
    return {
        "percent-outgoing-bytes": input['net_io_counters_eth0-bytes_sent']/byte_sum,
        "percent-memory-caching": memory_caching_content/input['virtual_memory-available'],
        **moving_mean_dict
    }