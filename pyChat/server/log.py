from datetime import datetime

class Logs:
    """
    Creates nice looking logs and prints them or saves to file
    """

    def __init__(self, file_src):
        self.file_src = file_src

    def create_log(self,message):
        """
        Retunrs message with date
        """

        now = datetime.now()
        time = now.strftime('%d/%m/%Y %H:%M:%S')

        log = f'[{time}] {message}'
        return log

    def log_to_file(self,message):
        """
        Creates a log and saves it to file
        """
        log = self.create_log(message)

        with open(self.file_src, 'a') as file:
            file.write(log + '\n')
            file.close()

    def log_to_print(self,message):
        """
        Creates a log and prints it
        """
        print(self.create_log(message))

    def log(self, message):
        """
        Creates a log, prints it and saves to file
        """
        
        self.log_to_file(message)
        self.log_to_print(message)
