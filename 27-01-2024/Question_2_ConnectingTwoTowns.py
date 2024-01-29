total_routes = 1 
    for route in routes:
        total_routes = (total_routes * route) % 1234567

    return total_routes
