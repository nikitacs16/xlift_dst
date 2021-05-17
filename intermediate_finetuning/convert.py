import sys
import random
import argparse
from tqdm import *
#from itertools import zip

random.seed(0)
def coin_toss():
	if random.random() < 0.5:
		return 1
	return 2
def parallel_dialogue():
	f3 = open(args.ofile, 'w')
	curr_count = 0
	while curr_count!=chat_count:
		k = random.randint(2,max_length)
		curr_lang = coin_toss()
		s = ""
		curr_c = 0
		with open(args.file1, "r") as f1, open(args.file2, "r") as f2:
			for index, (line_R1, line_R2) in tqdm(enumerate(zip(f1, f2))):
				if curr_c!=k:
					if curr_lang == 1:
						s = s + " " + line_R1.strip() 
					else:
						s = s + " " + line_R2.strip()
					curr_c = curr_c + 1
				else:
					if curr_lang != 1:
						s = s + " " + line_R1.strip()
					else:
						s = s + " " + line_R2.strip()
					
					if len(s.split()) < 512:
						curr_count = curr_count + 1
						f3.write(s.strip()+'\n')
						if curr_count >=chat_count:
							break

					curr_c = 0
					curr_lang = coin_toss()
					s = ""
					k = random.randint(2,max_length)

		f1.close()
		f2.close()


def response_dialogue():
        f3 = open(args.ofile, 'w')
        curr_count = 0
        while curr_count!=chat_count:
                k = random.randint(2,max_length)
                curr_lang = coin_toss()
                s = ""
                curr_c = 0
                with open(args.file1, "r") as f1, open(args.file2, "r") as f2:
                        for index, (line_R1, line_R2) in tqdm(enumerate(zip(f1, f2))):
                                if curr_c!=k:
                                        if curr_lang == 1:
                                                s = s + " " + line_R1.strip() 
                                        else:
                                                s = s + " " + line_R2.strip()
                                        curr_c = curr_c + 1
                                else:
                                        if curr_lang != 1:
                                                s = s + " <S> " + line_R1.strip()
                                        else:
                                                s = s + " <S> " + line_R2.strip()

                                        if len(s.split()) < 512:
                                                curr_count = curr_count + 1
                                                f3.write(s.strip()+'\n')
                                                if curr_count >=chat_count:
                                                        break

                                        curr_c = 0
                                        curr_lang = coin_toss()
                                        s = ""
                                        k = random.randint(2,max_length)

                f1.close()
                f2.close()



def single_dialogue():
	f3 = open(args.ofile, 'w')
	curr_count = 0
	while curr_count!=chat_count:
		k = random.randint(2,max_length)
		s = ""
		curr_c = 0
		with open(args.file1, "r") as f1:
			for line_R1 in f1:
				s = s + " " + line_R1.strip() 
				curr_c = curr_c + 1
				if curr_c == k:
					if len(s.split()) < 512:
						curr_count = curr_count + 1
						f3.write(s.strip()+'\n')
						if curr_count >=chat_count:
							break
					curr_c = 0
					s = ""
					k = random.randint(2,max_length)

		f1.close()


def mixed_dialogue():

	f3 = open(args.ofile, 'w')
	curr_count = 0
	while curr_count!=chat_count:
		k = random.randint(2,max_length)
		s = ""
		curr_c = 0
		set_flag = False
		with open(args.file1, "r") as f1, open(args.file2, "r") as f2:
			for index, (line_R1, line_R2) in tqdm(enumerate(zip(f1, f2))):
				if not set_flag: 
					curr_lang = coin_toss()

				if curr_c!=k:
					if curr_lang == 1:
						s = s + " " + line_R1.strip() 
					else:
						s = s + " " + line_R2.strip()
					curr_c = curr_c + 1
				else:				
					if len(s.split()) < 512:
						curr_count = curr_count + 1
						f3.write(s.strip()+'\n')
						if curr_count >=chat_count:
							break

					curr_c = 0
					s = ""
					k = random.randint(2,max_length)
					set_flag = coin_toss()
					if set_flag == 1:
						set_flag = True
						curr_lang = coin_toss()
					else:
						set_flag = False

		f1.close()
		f2.close()
	f3.close()

def tlm_dialogue():
	f3 = open(args.ofile, 'w')
	curr_count = 0
	max_length = 8
	while curr_count!=chat_count:
		k = random.randint(2,max_length)
		curr_lang = coin_toss()
		s = ""
		t = ""
		curr_c = 0
		with open(args.file1, "r") as f1, open(args.file2, "r") as f2:
			for index, (line_R1, line_R2) in tqdm(enumerate(zip(f1, f2))):
				if curr_c!=k:
					s = s + " " + line_R1.strip() 
					t = t + " " + line_R2.strip()
					curr_c = curr_c + 1
				else:
					s = s + " " + line_R1.strip()
					t = t + " " + line_R2.strip()
					if len(s.split()) < 256:
							curr_count = curr_count + 1
							if curr_lang ==1:
								s = t + " " + s
							else:
								s = s + " " + t
							f3.write(s.strip()+'\n')
							if curr_count >=chat_count:
									break

					curr_c = 0
					curr_lang = coin_toss()
					s = ""
					t = ""
					k = random.randint(2,max_length)

		f1.close()
		f2.close()

def bilingual_dialogue():
	f3 = open(args.ofile, 'w')
	curr_count = 0
	while curr_count!=chat_count:
		k = random.randint(2,max_length)
		curr_lang = coin_toss()
		s = ""
		curr_c = 0
		with open(args.file1, "r") as f1, open(args.file2, "r") as f2:
			for index, (line_R1, line_R2) in tqdm(enumerate(zip(f1, f2))):
				if curr_c!=k:
					if curr_lang == 1:
							s = s + " " + line_R1.strip() 
					else:
							s = s + " " + line_R2.strip()
					curr_c = curr_c + 1
				else:
					if curr_lang == 1:
							s = s + " " + line_R1.strip()
					else:
							s = s + " " + line_R2.strip()
					
					if len(s.split()) < 512:
							curr_count = curr_count + 1
							f3.write(s.strip()+'\n')
							if curr_count >=chat_count:
									break

					curr_c = 0
					curr_lang = coin_toss()
					s = ""
					k = random.randint(2,max_length)

		f1.close()
		f2.close()





parser = argparse.ArgumentParser(description='Process to chat-level files')
parser.add_argument('--file1',  type=str, help='First file to process')
parser.add_argument('--file2',  type=str, nargs="?")
parser.add_argument('--ofile',  type=str) 
parser.add_argument('--parallel', action='store_true')
parser.add_argument('--single', action='store_true')
parser.add_argument('--mixed', action='store_true')
parser.add_argument('--tlm', action='store_true')
parser.add_argument('--bidm', action='store_true')
parser.add_argument('--response', action='store_true')
parser.add_argument('--count', type=int)

args = parser.parse_args()
chat_count = args.count
max_length = 15

if args.parallel:
	parallel_dialogue()
if args.mixed:
	mixed_dialogue()
if args.single:
	single_dialogue()
if args.tlm:
	tlm_dialogue()
if args.bidm:
	bilingual_dialogue()

if args.response:
	response_dialogue()
