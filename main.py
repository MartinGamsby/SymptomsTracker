import os
import subprocess

import report


def run_cmd(arg):
    args = arg.split()
    args = [os.path.expandvars(i) for i in args]
    subprocess.run(args)

    
def main():
    print("pdf start")
    report.generate_pdf(patient_name="Martin Gamsby",
        summary_text="test")
    print("pdf end")
    run_cmd("cmd.exe /c start output\\report.pdf")
    #run_cmd("explorer.exe output")


if __name__ == "__main__":
    main()
