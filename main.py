import tkinter
import tkinter.filedialog
from numpy import hanning, hamming
from scipy.signal.windows import flattop

from plots import plot_time, plot_frequency, plot_waterfall, PlotRange
from record import record
from math_operations import calculate_material_properties


# Parameters
FS = 44100
DURATION = 3
is_log_scale = False
plot_range = PlotRange(x=None, y=None)

window_functions = {
    "None": None,
    "Hanning": hanning,
    "Hamming": hamming,
    "Flattop": flattop,
}


def start_recording():
    """
    This function is connected with Record button. It starts recording, cretracting plots, showing fundamental resonant frequency and craeting .xslx file.
    """
    global FS, plot_range

    duration = float(get_duration_from_user.get())
    if duration <= 0:
        raise ValueError("Durations must be positive")

    recording = record(duration, FS)  # start recording

    waterfall = plot_waterfall(
        recording, FS, window_functions, window_function_choice
    )  # creating plot object for waterfall plot
    freq, max_freq = plot_frequency(
        recording,
        FS,
        is_log_scale,
        plot_range,
        window_functions,
        window_function_choice,
    )  # creating plot object for frequency plot
    time = plot_time(recording, FS)  # creating plot object for time plot
    result_window_max_freq(
        max_freq
    )  # showing window with fundamental resonant frequency
    time.show()  # showing plot object for waterfall plot
    freq.show()  # showing plot object for waterfall plot
    waterfall.show()  # showing plot object for waterfall plot


def update_plot_range():
    """
    This function updates plot axis ranges if provided. If not provided, the function set axis ranges as None values.
    """
    global plot_range

    # Operations for x-axis
    zakres_x_start = get_first_x_range_from_user.get()
    zakres_x_end = get_second_x_range_from_user.get()
    if not zakres_x_start == "" and not zakres_x_end == "":
        plot_range.x = (float(zakres_x_start), float(zakres_x_end))
    else:
        plot_range.x = None

    # Operations for y-axis
    zakres_y_start = get_first_y_range_from_user.get()
    zakres_y_end = get_second_y_range_from_user.get()
    if not zakres_y_start == "" and not zakres_y_end == "":
        plot_range.y = (float(zakres_y_start), float(zakres_y_end))
    else:
        plot_range.y = None


def result_window_max_freq(max_freq):
    """
    This function craete new window, with value of the fundamental resonant frequency.
    """
    window = tkinter.Toplevel()
    window.geometry("300x50")

    label = tkinter.Label(window, text="Result:")
    label.pack()

    max_frequency = tkinter.Label(
        window, text=f"Fundamental resonant frequency : {max_freq}"
    )
    max_frequency.pack()


def computing_window():
    """
    This function creates a new window with as API where user can type in parameters as Young's modulus, Dynamic Shear Modulus and Poisson's Ratio.
    """
    window = tkinter.Toplevel()
    window.geometry("400x330")

    parameters_label = tkinter.Label(window, text="Insert data:")
    parameters_label.pack(pady=10)

    L_label = tkinter.Label(window, text="Length of the sample:")
    L_label.pack()
    get_L = tkinter.Entry(window)
    get_L.pack()

    b_label = tkinter.Label(window, text="Width of the sample:")
    b_label.pack()
    get_b = tkinter.Entry(window)
    get_b.pack()

    m_label = tkinter.Label(window, text="Mass of the sample:")
    m_label.pack()
    get_m = tkinter.Entry(window)
    get_m.pack()

    t_label = tkinter.Label(window, text="Thickness of the sample:")
    t_label.pack()
    get_t = tkinter.Entry(window)
    get_t.pack()

    f_f_label = tkinter.Label(window, text="f_f:")
    f_f_label.pack()
    get_ff = tkinter.Entry(window)
    get_ff.pack()

    f_t_label = tkinter.Label(window, text="f_t:")
    f_t_label.pack()
    get_ft = tkinter.Entry(window)
    get_ft.pack()

    def _calculate_properties():
        """
        This function get values typed by user to compute Young's modulus, Dynamic Shear Modulus and Poisson's Ratio and call function to calculate them.
        """
        L = float(get_L.get())
        b = float(get_b.get())
        m = float(get_m.get())
        t = float(get_t.get())
        f_f = float(get_ff.get())
        f_t = float(get_ft.get())

        result = calculate_material_properties(L, b, m, t, f_f, f_t)

        result_window = tkinter.Toplevel()
        result_window.geometry("300x200")

        result_label = tkinter.Label(result_window, text="Results:")
        result_label.pack(pady=10)

        youngs_modulus_label = tkinter.Label(
            result_window, text=f"Young's modulus: {result[0]}"
        )
        youngs_modulus_label.pack()

        dynamic_shear_modulus_label = tkinter.Label(
            result_window, text=f"Dynamic Shear Modulus: {result[1]}"
        )
        dynamic_shear_modulus_label.pack()

        poisson_ratio_label = tkinter.Label(
            result_window, text=f"Poisson's Ratio: {result[2]}"
        )
        poisson_ratio_label.pack()

    compute_button = tkinter.Button(
        window, text="Compute", command=_calculate_properties
    )
    compute_button.pack(pady=10)


def check_if_logarithmic_scale():
    """
    This function get the value, if the logarithmic scale is enabled.
    """
    global is_log_scale
    is_log_scale = logarithmic_checkbox_bool.get()


# Main screen initialization
root = tkinter.Tk()
root.title("Quick measurements of mechanical properties")
root.geometry("780x480")

# Record button
start_recording_button = tkinter.Button(
    root, text="Record", command=start_recording, width=30, height=10
)
start_recording_button.grid(row=0, column=0, padx=10, pady=20)

# Button for computing Young's modulus, Dynamic Shear Modulus and Poisson's Ratio
compute_button = tkinter.Button(
    root,
    text="Compute Young's modulus, Dynamic Shear Modulus and Poisson's Ratio",
    command=computing_window,
    width=15,
    height=10,
    wraplength=100,
)
compute_button.grid(row=0, column=1, padx=20, pady=20)

# Checkbox for logarithmic scale option
logarithmic_checkbox_bool = tkinter.BooleanVar(value=is_log_scale)
checkbox = tkinter.Checkbutton(
    root,
    text="Logarithmic scaling",
    variable=logarithmic_checkbox_bool,
    command=check_if_logarithmic_scale,
)
checkbox.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Record duration from user
duration_label = tkinter.Label(root, text="Duration (s):")
duration_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

get_duration_from_user = tkinter.Entry(root, width=10)
get_duration_from_user.grid(row=2, column=1, padx=10, pady=10, sticky="w")
get_duration_from_user.insert(tkinter.END, str(DURATION))

# Window function from user
window_function_label = tkinter.Label(root, text="Window function:")
window_function_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

window_choices = list(
    window_functions.keys()
)  # list of keys from window_functions dict
window_function_choice = tkinter.StringVar(root)
window_function_choice.set(window_choices[0])  # set default value as 'None'

window_funtion_dropdown_menu = tkinter.OptionMenu(
    root, window_function_choice, *window_choices
)
window_funtion_dropdown_menu.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# X axis range from user
range_x_label = tkinter.Label(root, text="Range x:")
range_x_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

get_first_x_range_from_user = tkinter.Entry(root, width=10)
get_first_x_range_from_user.grid(row=4, column=1, padx=5, pady=10, sticky="w")
if plot_range.x is not None:
    get_first_x_range_from_user.insert(tkinter.END, str(plot_range.x[0]))

get_second_x_range_from_user = tkinter.Entry(root, width=10)
get_second_x_range_from_user.grid(row=4, column=1, padx=5, pady=10, sticky="e")
if plot_range.x is not None:
    get_second_x_range_from_user.insert(tkinter.END, str(plot_range.x[1]))

# Y axis range from user
range_y_label = tkinter.Label(root, text="Range y:")
range_y_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

get_first_y_range_from_user = tkinter.Entry(root, width=10)
get_first_y_range_from_user.grid(row=5, column=1, padx=5, pady=10, sticky="w")
if plot_range.y is not None:
    get_first_y_range_from_user.insert(tkinter.END, str(plot_range.y[0]))

get_second_y_range_from_user = tkinter.Entry(root, width=10)
get_second_y_range_from_user.grid(row=5, column=1, padx=5, pady=10, sticky="e")
if plot_range.y is not None:
    get_second_y_range_from_user.insert(tkinter.END, str(plot_range.y[1]))

# Button for confirm axis ranges
update_range_button = tkinter.Button(root, text="Set range", command=update_plot_range)
update_range_button.grid(row=6, column=1, padx=10, pady=10)

# Vertical separating line
separating_line = tkinter.Frame(root, width=2, bg="black")
separating_line.grid(row=0, column=2, rowspan=7, sticky="ns", padx=10, pady=10)

# Text box with instructions
instructions_text_field_label = tkinter.Label(
    root,
    text="Before measurement:\n\n1. Check or uncheck the logarithmic scaling option depending on whether you want the plot to be scaled logarithmically or not.\n\n2. Set the duration of the measurement as a positive integer value.\n\n3. Choose a window function for the plot. You can leave it as None if you don't want to use any specific window function.\n\n4. Select the ranges for the x and y axes. If you leave the values blank, the program will automatically adjust the ranges. The range values should be real numbers without any white spaces. For specifying a range, provide both the minimum and maximum values. Leaving either of them blank will result in automatic range selection by the program.\n\n5. The option 'Compute Young's modulus, Dynamic Shear Modulus and Poisson's Ratio' allows you to calculate the Young's modulus, elastic modulus, and Poisson's ratio after entering the appropriate data.",
    font=("Arial", 10),
    justify="left",
    wraplength=350,
)
instructions_text_field_label.grid(
    row=0, column=3, rowspan=7, padx=10, pady=10, sticky="w"
)


root.mainloop()
