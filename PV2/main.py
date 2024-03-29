from teacher import TeacherCRUD

uri = "bolt://52.90.188.81:7687"
user = "neo4j"
password = "corps-boxcars-conspiracies"

teacher_crud = TeacherCRUD(uri, user, password)

teacher_crud.create("Chris Lima", 1956, "189.052.396-66")

teacher = teacher_crud.read("Chris Lima")
if teacher:
    print("Teacher encontrado:")
    print(teacher)
else:
    print("Teacher não encontrado.")

teacher_crud.update("Chris Lima", "162.052.777-77")

teacher_crud.close_database()
