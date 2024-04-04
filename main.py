import delete
import run_threads
import taking_photo

from interactive_demo import xmem_interactive

def main():

    delete.main()

    folder_name = taking_photo.main()
    xmem_interactive(folder_name)
    
    run_threads.main(folder_name)

if __name__ == "__main__":
    main()