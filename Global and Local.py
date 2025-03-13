x=4
print(f"Before modifying x:{x}")
def Hello():
    global x
    x=5  # modifyimg global x value
    print(f"1 after modifying x:{x}")
Hello()
print(f"2 after modifying x:{x}")
