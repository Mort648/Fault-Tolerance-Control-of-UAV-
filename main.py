def simulate(ftc_enabled=False):
    # Initial conditions
    z = 0.0
    vz = 0.0
    theta = 0.0
    omega = 0.0

    z_hist = []
    theta_hist = []

    # PID state
    e_z_int = 0
    e_z_prev = 0
    e_theta_int = 0
    e_theta_prev = 0

    for i in range(N):
        t_now = i * dt
        # PID control for altitude
        e_z = z_target - z
        e_z_int += e_z * dt
        de_z = (e_z - e_z_prev) / dt
        u_z = Kp_z * e_z + Ki_z * e_z_int + Kd_z * de_z
        e_z_prev = e_z
        F_total = m * g + u_z
        F_total = np.clip(F_total, 0, 20)

        # PID control for angle
        e_theta = theta_target - theta
        e_theta_int += e_theta * dt
        de_theta = (e_theta - e_theta_prev) / dt
        u_theta = Kp_theta * e_theta + Ki_theta * e_theta_int + Kd_theta * de_theta
        e_theta_prev = e_theta
        torque = u_theta
        F_diff = torque / L

        # --- Motor force allocation ---
        fault = t_now > 0.5

        if fault and ftc_enabled:
            # With fault-tolerant logic
            F1 = (F_total - F_diff * 0.3) / 2
            F2 = (F_total + F_diff * 1.7) / 2
        else:
            # Normal or fault without FTC
            F1 = (F_total - F_diff) / 2
            F2 = (F_total + F_diff) / 2
            if fault and not ftc_enabled:
                F1 *= 0.5  # simulate fault

        F1 = np.clip(F1, 0, 15)
        F2 = np.clip(F2, 0, 15)

        # Physics update
        a = (F1 + F2 - m * g) / m
        vz += a * dt
        z += vz * dt

        torque = (F2 - F1) * L
        alpha = torque / I
        omega += alpha * dt
        theta += omega * dt

        z_hist.append(z)
        theta_hist.append(np.degrees(theta))  # convert to degrees

    return z_hist, theta_hist
