midterms = [80, 91, 78]

finals = [98, 89, 53]

students = ['Dan', 'Ang', 'Kate']

final_grades = { t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}

print(final_grades)


grades = dict(zip(students, map(
            lambda pair: max(pair), 
            zip(midterms, finals)
             )
        )
)

print(grades)