n = int(input())
s = input()
st = []
ans = 0

for c in s:
    if c == "(":
        st.append(c)
    else:
        if st:
            st.pop()
        else:
            ans+=1
            st.append("(")
print(ans)

