'''
Created on Sep 4, 2016

@author: Tom
'''

import sys, fileinput, time, traceback


def solve(in_str, test, filename):
    
    str_len = len(in_str)
    count = 0
    if in_str[0].islower():
        count += 1
        for i in range(1, str_len - 1):
            if in_str[i].isupper():
                count += 1
     
    result = count

    if filename is None:
        print (result)

    if filename is not None:
        output_file = open(filename, 'a')
        output_file.write(str(result)) 
        output_file.close()

def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True

def isNotBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return True
    #myString is None OR myString is empty or blank
    return False

def main():

    arg = False

    test = 0
    arg_list = len(sys.argv)

    if arg_list > 1:
        test = -1
        arg = True
        test_filename = None

        for line in fileinput.input():

            
            inp = line.split()
            input_str = inp[0]
            #input_str = line
            
            test_filename = fileinput.filename()
            test_filename = "test_" + test_filename
            output_file = open(test_filename, 'w')
            output_file.write("")
            output_file.close()

            solve(input_str, test, test_filename)

            #if cases == test_lines:
                #cases_read = False
                
            test+= 1
            
            test_file = open(test_filename, 'r')
            if test < 11:
                hr_filename = "output0" + str(test) +".txt"
            else:
                hr_filename = "output" + str(test) +".txt"
                
            print("\n test =", test_filename, " hr = ", hr_filename)

            hr_file = open(hr_filename,'r')

            passed = True

            test_line = test_file.readline()
            hr_line = hr_file.readline()

            while  isNotBlank(test_line) and isNotBlank(hr_line) :
                #if "\n" == test_line[-1] or "\n" == hr_line[-1]:
                    #break
                ##print("\ntest = ", test_line, " hr = ", hr_line)
                #test_int = int(test_line)
                #hr_int = int(hr_line)
                if test_line != hr_line:
                    passed = False
                test_line = test_file.readline()
                hr_line = hr_file.readline()

            if passed == True:
                print("\nTest " + str(test) + " passed")
            else:
                print("\nTest " + str(test) + " failed")

            test_file.close()
            hr_file.close()


    if arg == False:
        filename = None
        test = None
        inp = input().strip()
        input_str = inp
            #print("inp = " , inp)
            #inp1 = input("Pause")
        solve(input_str, test, filename)
       

if __name__  ==  '__main__':
    #main()
    t = time.time()
    try:
        main()
    except Exception as e:
        print ("\nFailure:", e)
        """exc_type, exc_value, exc_traceback = sys.exc_info() # most recent (if any) by default
        traceback_details = {
                         'filename': exc_traceback.tb_frame.f_code.co_filename,
                         'lineno'  : exc_traceback.tb_lineno,
                         'name'    : exc_traceback.tb_frame.f_code.co_name,
                         'type'    : exc_type.__name__,
                         'message' : e.message, # or see traceback._some_str()
                        }

        del(exc_type, exc_value, exc_traceback) # So we don't leave our local labels/objects dangling"""
        exc_type, exc_value, exc_tb = sys.exc_info()
        filename, line_num, func_name, text = traceback.extract_tb(exc_tb)[-1]
        print ('Thrown from: %s line %s' % (filename,  line_num))
    exec_time = time.time() - t
    print("Finished camelcase.py")
    runfile = "camelcase.py"
    print ("\nExecution time: ", str(exec_time), "seconds")
    runtime_file = "runtimes.txt"
    runtime = open(runtime_file, 'a')
    run_str = runfile + "\t\t" + "Execution time: " + str(exec_time) + " seconds\n"
    runtime.write (run_str)
    runtime.close()    