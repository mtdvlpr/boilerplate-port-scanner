import socket

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    try:
        ip = socket.gethostbyname(target)
        hostname = None
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            pass
    except socket.gaierror:
        if target.replace('.', '').isdigit():
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"

    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)

    if verbose:
        result = f"Open ports for {hostname or ip} ({ip})\n" if hostname else f"Open ports for {ip}\n"
        result += "PORT     SERVICE\n"
        for port in open_ports:
            service = socket.getservbyport(port, "tcp") if port in open_ports else "unknown"
            result += f"{port:<9}{service}\n"
        return result.strip()

    return open_ports
