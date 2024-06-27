# Imports and such
from datetime import datetime
from typing import Dict
import logging
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MoistureSensor:
    """
    A class to encapsulate a single moisture sensor.
    """
    def __init__(self) -> None:
        """
        Initialises the sensor
        """
        self.last_moisture = self.get_data()
        self.last_moisture_timestamp = datetime.now()
    
    def get_data(self) -> float:
        """
        Gets the moisture value from this sensor.

        Returns:
            float: The moisture level
        """

        # TODO: figure out how to read value from sensor

        # Update the sensor's last reading value
        self.last_moisture = None # TODO: Set to the read value when available
        # Update the sensor's last reading timestamp
        self.last_moisture_timestamp = datetime.now()
        
        pass # incomplete function, Pass.

class TemperatureSensor:
    """
    A class to encapsulate a single temperature sensor.
    """
    def __init__(self) -> None:
        """
        Initialises the sensor
        """
        self.last_temperature = self.get_data()
        self.last_temperature_timestamp = datetime.now()
    
    def get_data(self) -> float:
        """
        Gets the moisture value from this sensor.

        Returns:
            float: The moisture level
        """

        # TODO: figure out how to read value from sensor

        self.last_temperature = None # TODO: set to the read value when available
        # Update the sensor's last reading timestamp
        self.last_temperature_timestamp = datetime.now()
        
        pass # Incomplete function, pass.

class Valve:
    """
    A class to encapsulate a single valve.
    """

    def __init__(self) -> None:
        """
        Initialises the valve
        """
        pass

    def open(self)-> None:
        """
        Opens the valve
        """
        pass

    def close(self) -> None:
        """
        Closes the valve
        """
        pass

    def open_for_time(self, time_in_seconds:int) -> None:
        # Open the valve
        self.open()
        # Wait
        time.sleep(time_in_seconds)
        # Close the valve
        self.close() 


class Bed:
    """
    A Class to encapsulate a single Bed of vegetables.
    """
    def __init__(self, plant_name:str, temperature_sensor:TemperatureSensor, moisture_sensor:MoistureSensor, valve:Valve) -> None:
        self.plant_name = plant_name
        self.temperature_sensor = temperature_sensor
        self.moisture_sensor = moisture_sensor
        self.valve = valve

    def get_current_bed_data(self) -> Dict[str:float]:
        """
        Fetches the current data from the bed's sensors.

        Returns:
            dict: A dictionary with sensor type keys and data values. 
        """

        return {'moisture': self.moisture_sensor.get_data(),
                'temperature':  self.temperature_sensor.get_data()
                }
    
    def water_bed(self, watering_time_in_seconds:int) -> None:
        """releases a valve to water the bed for a specified number of seconds.

        Args:
            watering_time_in_seconds (int): The number of seconds to water the bed for.
        """

        self.valve.open_for_time(watering_time_in_seconds)
        pass
        

class WaterLevelHandler:
    """
    A Class encapsulating the functionality of a water handler and its related email system.
    """


    def __init__(self) -> None:

        
        self.last_email_date_time = None
        
        self.water_low_beginning_date_time = None

        # Set the threshold value for this sensor. Any lower than this and the water is 'low'.
        self.threshold_value = None # TODO: Figure out a water threshold value from the raw sensor data.

        #TODO: Set up water sensor 
        pass

    def send_email(self, receiver_email:str, subject:str, message:str) -> None:
        """
        Sends an email to a specified email with a specific message.

        Args:
            receiver_email (str): The email to send the message to
            message (str): The message to send.
        """

        # Set the smtp#TODO: Set up water sensor  server address
        smtp_server = '' #TODO: Add the server address 
        # Set the smtp server port to 587 for TLS.
        smtp_port = 587
        # Set the sender email
        sender_email = '' #TODO: Set an email to use 
        # Set the sender password
        password = None #TODO: Use a password from a config file.

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))


        try:
            # Connect to the server
            server = smtplib.SMTP(smtp_server, smtp_port)
            # Secure the connection
            server.starttls()
            # Log into the server
            server.login(sender_email, password)
            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())
            
            #TODO: print a confirmation message?
        except Exception as e:
            print(f'Error: {e}')
        finally:
            # Close server connection
            server.quit() 

        #TODO: send a message to the specified email.

        # Set last email datetime to current datetime.
        self.last_email_date_time = datetime.now()

        pass


    def check_water_level_is_sufficient(self) -> bool:
        """
        Checks if the water level is above or below the sensor.

        Returns:
            bool: True if the sensor is covered in water, False of it's not.
        """
        


        # Get the sensor's raw data.
        sensor_output = None # TODO: implement level fetching


        if sensor_output < self.threshold_value:
            
            # Check it hasn't been 3 days since the water was first low.
            if self.water_low_beginning_date_time != None:
                difference = datetime.now() - self.water_low_beginning_date_time
                difference_in_seconds = difference.total_seconds()
                
                # 
                if difference_in_seconds >= 259200:
        
        


        pass




# --- Driver code ---
def main():

    running = True # Create running flag.

    # Main irrigation loop.
    while running:
        
        pass


        

if __name__ == '__main__':
    main()
