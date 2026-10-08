from log_write import write_log


def main():
    while True:
        text = input('Give input or type "exit" to end:\n')

        if text.strip().lower() == "exit":
            break

        write_log(text)
    write_log('Exiting program')


if __name__ == "__main__":
    main()