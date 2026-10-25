class LagBalancer:
    def __init__(self, base_health=100, target_ping=500, max_bonus_multiplier=1.25):
        """
        base_health: The standard HP for a flawless connection (0-30ms).
        target_ping: The ping threshold where maximum compensation is reached.
        max_bonus_multiplier: The percentage of extra health given at target_ping (1.25 = +125% health).
        """
        self.base_health = base_health
        self.target_ping = target_ping
        self.max_bonus_multiplier = max_bonus_multiplier

    def calculate_compensated_health(self, current_ping):
        """
        Calculates exact player health dynamically based on current network latency.
        """
        # Clamp ping to avoid negative values or infinite scaling
        current_ping = max(0, current_ping)
        
        # Ping below 30ms is considered 'perfect' and gets no bonus
        if current_ping <= 30:
            return self.base_health
        
        # Cap the scaling calculations at our target high ping limit
        effective_ping = min(current_ping, self.target_ping)
        
        # Progressive scaling factor (0.0 to 1.0)
        # Using a soft quadratic curve prevents low-latency spikes from skewing balance
        scaling_ratio = (effective_ping / self.target_ping) ** 1.5
        
        # Determine the total bonus health points
        max_bonus_hp = self.base_health * self.max_bonus_multiplier
        calculated_bonus = max_bonus_hp * scaling_ratio
        
        # Final Total Health
        total_health = round(self.base_health + calculated_bonus)
        return total_health

# --- SIMULATION & VERIFICATION ---
if __name__ == "__main__":
    balancer = LagBalancer(base_health=100, target_ping=500, max_bonus_multiplier=1.25)
    
    # Test network conditions across different global regions
    test_pings = [20, 60, 150, 280, 500, 750]
    
    print("=== LIVE NETWORK HEALTH LOGS ===")
    for ping in test_pings:
        hp = balancer.calculate_compensated_health(ping)
        bonus = hp - 100
        print(f"Ping: {ping:3d}ms | Adjusted Health: {hp:3d} HP (+{bonus} HP Buffer)")
