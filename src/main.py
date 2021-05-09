from file_handler.directory import Directory
from frame_calculations.frame_factory import FrameFactory

raw_folder = '../april_2021/APR 21/'
final_folder = '../april_2021/final_154/'
raw_directory = Directory(raw_folder)
final_directory = Directory(final_folder)


if __name__ == '__main__':
    if raw_directory.are_files_matching(final_directory):
        for file in raw_directory[0:1]:
            df = FrameFactory.create_frame(
                directory=raw_directory, file=file).df
            print(df.head())
