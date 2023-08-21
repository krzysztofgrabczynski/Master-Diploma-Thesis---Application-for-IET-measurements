# <p align=center> <a name="top">Master-Diploma-Thesis---Application-for-IET-measurements </a></p>  

## Description
The main function of the app is using an external microphone and the IET (Impulse Excitation Technique) to detect the frequency response of metal samples to determine their quality and basic mechanical properties.

The application can take measurements with a microphone (the duration of the measurement is modifiable from the GUI level). It allows you to select parameters such as logarithmic scaling of graphs, use of available window functions as well as specifying the ranges of the X and Y axes. The results are presented in the form of graphs: sound pressure, FFT Magnitude 2D and FFT Magnitude 3D. We also get the result of the fundamental resonant frequency, which we can then use to calculate the mechanical properties, also using that app.

This app was created for educational purposes (Master Diploma Thesis).

If you want to check out my other projects [click here.](https://github.com/krzysztofgrabczynski)

## Preview
The main window of the application, which allows you to perform the measurement, select parameters, turn on the window to perform mathematical calculations of mechanical properties, as well as a short application manual.
<p align="center">
  <img src="https://github.com/krzysztofgrabczynski/Master-Diploma-Thesis---Application-for-IET-measurements/assets/90046128/90035b0d-eda8-45ce-b215-0190b6284851">
</p>

The window used for calculations of mechanical properties, after entering the data, the calculation result is displayed (f_f and f_t are obtained as the result of measurements made with a microphone).
<p align="center">
  <img src="https://github.com/krzysztofgrabczynski/Master-Diploma-Thesis---Application-for-IET-measurements/assets/90046128/5fce890f-5edc-482d-822c-8bb04df58821">
</p>

Resulting graphs, from which the excitation of the material to vibrations can be observed, and the dominant frequencies can be read.
<p align="center">
  <img src="https://github.com/krzysztofgrabczynski/Master-Diploma-Thesis---Application-for-IET-measurements/assets/90046128/30b14641-f1c9-47b8-9119-8df1a3a303a5" width="500">
  <img src="https://github.com/krzysztofgrabczynski/Master-Diploma-Thesis---Application-for-IET-measurements/assets/90046128/e710fa0a-c22e-47f7-b1ea-8cba2bb1a542" width="500">
</p>

Magnitude FFT 3D result plot that shows the value of the dominant frequency over time and its amplitude.
<p align="center">
  <img src="https://github.com/krzysztofgrabczynski/Master-Diploma-Thesis---Application-for-IET-measurements/assets/90046128/4e57b97e-bd6d-4fd5-bd4c-a980ebacd29e">
</p>

## Procedure

- sample preparation (e.g. steel) for measurements
- laying the material on the supports and preparing a stand with a microphone
- excitation of the sample (e.g. with a small hammer)
- read the result of the fundamental resonant frequency
- repeat the steps for the changed support position for the next mode
- read the result of the fundamental resonant frequency in next mode]
- substitute the results for mathematical calculations


## Install for local use 
- Copy the repository
- Create virtual environment using ``` python -m venv venv ``` in project directory
- Use ``` . venv/Scripts/activate ``` to activate the virtual environment
- Install required packages by ``` pip install -r requirements.txt ```
- Enter the ``` python manage.py migrate --run-syncdb ``` to update migrations
- Now, you can run the application with this: ``` python manage.py runserver ```
- Everything done! You can open Instagram app in your browser by ctrl + left click on http link in your console

[Go to top](#top) 
