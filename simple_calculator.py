while True :
        op=input("\t~~ Main ~~\n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit\nEnter option:")
        d={"1":"+",'2':"-",'3':"*",'4':"/"}
        n1,n2=input("Enter 2 number:").split(" ") if op in d else exit("end of code")
        print(f'Result :{eval(f" {n1} {d.get(op)} {n2}")}')