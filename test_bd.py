import psycopg2

conexao = psycopg2.connect("dbname=store user=postgres password=admin")
cursor = conexao.cursor()

customer = {}
customers = {}
listCustomers = []

customer['id'] = "1"
customer['name'] = "Rafael"
customer['fullname'] = "Rafael Costa Teixeira"
customer['birth'] = "06/05/1982"
customer['document'] = "31657287807"
customer['gender'] = 'Male'
#listCustomers.append(customer)
cursor.execute("insert into Customers (name,fullname,birth,document,gender) values('"+customer['name']+"','"+customer['fullname']+"',to_date('"+customer['birth']+"','MM/DD/YYYY'),'"+customer['document']+"','"+customer['gender'][0]+"')")
conexao.commit()

customer = {}
customer['id'] = "2"
customer['name'] = "Marlene"
customer['fullname'] = "Marlene Costa"
customer['birth'] = "02/12/1957"
customer['document'] = "23412356780"
customer['gender'] = 'Female'

#listCustomers.append(customer)
cursor.execute("insert into Customers (name,fullname,birth,document,gender) values('"+customer['name']+"','"+customer['fullname']+"',to_date('"+customer['birth']+"','MM/DD/YYYY'),'"+customer['document']+"','"+customer['gender'][0]+"')")
conexao.commit()
cursor.close()

#customers['customers'] = listCustomers

#return customers



