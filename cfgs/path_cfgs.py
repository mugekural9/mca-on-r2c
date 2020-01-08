import os

class PATH:
    def __init__(self):

        self.DATASET_PATH = './datasets/r2c/'
        self.FEATURE_PATH = './datasets/r2c/'

        self.init_path()


    def init_path(self):

        self.IMG_FEAT_PATH = {
            'train': self.FEATURE_PATH + 'train2019/'
        }

        self.QAR_PATH = {
            'train': self.DATASET_PATH + 'r2c_qar.jsonl'
        }

        self.CKPTS_PATH = './ckpts/'

        if 'ckpts' not in os.listdir('./'):
            os.mkdir('./ckpts')


    def check_path(self):
        print('Checking dataset ...')
     
        for mode in self.QAR_PATH:
            if not os.path.exists(self.QAR_PATH[mode]):
                print(self.QAR_PATH[mode] + 'NOT EXIST')
                exit(-1)

        print('Finished')
        print('')

