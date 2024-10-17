class Role:
    ADMIN = 'admin'
    TECHNICIAN = 'technician'
    OPERATOR = 'operator'
    USER = 'user'

    CHOICES = [
        (ADMIN, 'Admin'),
        (TECHNICIAN, 'Technician'),
        (OPERATOR, 'Operator'),
        (USER, 'Regular User'),
    ]