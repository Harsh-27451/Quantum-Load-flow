import numpy as np
from load_flow import load_flow, calculate_loss, convert_to_pu
from data import line_data, load_data, tie_lines


def evaluate(line_data):
    line_data_pu = convert_to_pu(line_data)
    V, I = load_flow(line_data_pu, load_data)
    return calculate_loss(line_data_pu, I)


def branch_exchange():

    base = np.array(line_data)
    base_loss = evaluate(base)

    print(f"Base Loss: {base_loss:.6f} pu")

    best_loss = base_loss
    best_config = None

    # Try each tie line
    for tie in tie_lines:

        temp = base.tolist()
        temp.append(tie)  # close tie switch

        # Try opening each original line
        for i in range(len(base)):

            new_config = temp.copy()
            removed_line = new_config.pop(i)  # open line

            try:
                loss = evaluate(np.array(new_config))

                # Keep best result
                if loss < best_loss:
                    best_loss = loss
                    best_config = {
                        "tie": tie,
                        "opened": removed_line
                    }

            except:
                continue

    # -----------------------------
    # PRINT RESULTS (CLEAN FORMAT)
    # -----------------------------
    print(f"\nBest Loss: {best_loss:.6f} pu")

    if best_config:
        tie = best_config["tie"]
        opened = best_config["opened"]

        print("\nOptimal Reconfiguration:")
        print(f"Close Tie Line : {int(tie[0])} - {int(tie[1])}")
        print(f"Open Line      : {int(opened[0])} - {int(opened[1])}")

    else:
        print("\nNo better configuration found.")


# Run function directly (optional)
if __name__ == "__main__":
    branch_exchange()