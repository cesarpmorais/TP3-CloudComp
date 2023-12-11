# Mocks mymodule.py functioning

class Mockers:
    @classmethod
    def get_input(cls):
        return {
            "timestamp": "2023-12-08T12:00:00",
            "cpu_freq_current": 3000.0,
            "cpu_percent-0": 10.5,
            "cpu_percent-1": 20.1,
            "cpu_stats-ctx_switches": 5000,
            "cpu_stats-interrupts": 200,
            "cpu_stats-soft_interrupts": 100,
            "cpu_stats-syscalls": 300,
            "n_pids": 50,
            "virtual_memory-total": 16777216,
            "virtual_memory-available": 8388608,
            "virtual_memory-percent": 50.0,
            "virtual_memory-used": 8388608,
            "virtual_memory-free": 8388608,
            "virtual_memory-active": 4194304,
            "virtual_memory-inactive": 4194304,
            "virtual_memory-buffers": 102400,
            "virtual_memory-cached": 204800,
            "virtual_memory-shared": 51200,
            "virtual_memory-slab": 409600,
            "net_io_counters_eth0-bytes_sent1": 1024000,
            "net_io_counters_eth0-bytes_recv1": 512000,
            "net_io_counters_eth0-packets_sent1": 1000,
            "net_io_counters_eth0-packets_recv1": 800,
            "net_io_counters_eth0-errin1": 5,
            "net_io_counters_eth0-errout1": 2,
            "net_io_counters_eth0-dropin1": 1,
            "net_io_counters_eth0-dropout1": 0
        }

    @classmethod
    def get_context(cls):
        return {
            "host": "redis-server-hostname",
            "port": 6379,
            "input_key": "metrics",
            "output_key": "ifs4-proj3-output",
            "function_getmtime": "2023-12-08T11:30:00",
            "last_execution": "2023-12-08T11:55:00",
            "env": {
                "moving_average_cpu0": 15.2,
                "moving_average_cpu1": 25.6,
                "custom_variable": "example_value"
            }
        }