def calibrate_output(verified_statements):
    """
    Adjusts the final output based on verification results.
    """
    calibrated_output = ""
    for stmt in verified_statements:
        if stmt.startswith("UNVERIFIED"):
            calibrated_output += "I'm not certain about the following statement:\n"
            calibrated_output += f"{stmt.replace('UNVERIFIED: ', '')}\n\n"
        else:
            calibrated_output += stmt + "\n"
    return calibrated_output
