def primery():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    print(quotes[0])

    f.close()

    print(quotes)

#if __name__== "__main__":
  #main()

