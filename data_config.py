
class DataConfig:
    data_name = ""
    root_dir = ""
    label_transform = "norm"
    def get_data_config(self, data_name):
        self.data_name = data_name
        if data_name.strip() == 'LEVIR':
            self.root_dir = 'path to the root of LEVIR-CD dataset'
        elif data_name.strip() == 'quick_start':
            self.root_dir = './samples/'
            print(self.root_dir)
        else:
            print("Data name received:", data_name)  # Add this line for debugging
            raise TypeError('%s has not defined' % data_name)
        return self


if __name__ == '__main__':
    data = DataConfig().get_data_config(data_name='LEVIR')
    print(data.data_name)
    print(data.root_dir)
    print(data.label_transform)
