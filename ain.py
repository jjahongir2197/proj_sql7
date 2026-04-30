-- Departments
INSERT INTO departments (id, name) VALUES
(1, 'IT'),
(2, 'Marketing'),
(3, 'Finance'),
(4, 'HR'),
(5, 'Sales');


-- Employees
INSERT INTO employees (id, firstname, lastname, department_id) VALUES
(1, 'Azamat', 'Tohirov', 1),
(2, 'Dilshod', 'Karimov', 2),
(3, 'Malika', 'Xasanova', 3),
(4, 'Jasur', 'Aliyev', 1),
(5, 'Nodira', 'Rahimova', 4),
(6, 'Sardor', 'Qodirov', 5),
(7, 'Zarina', 'Yusupova', 2),
(8, 'Bekzod', 'Tursunov', 3);


-- Projects
INSERT INTO projects (id, title, employee_id) VALUES
(1, 'CRM System', 1),
(2, 'Ad Campaign', 2),
(3, 'Budget Plan', 3),
(4, 'Website Redesign', 4),
(5, 'Hiring System', 5),
(6, 'Sales Boost', 6);


-- Tasks
INSERT INTO tasks (id, name, project_id) VALUES
(1, 'Backend yozish', 1),
(2, 'Frontend qilish', 1),
(3, 'Reklama dizayni', 2),
(4, 'SMM yuritish', 2),
(5, 'Hisobot tayyorlash', 3),
(6, 'Analiz qilish', 3),
(7, 'UI/UX design', 4),
(8, 'Interview olish', 5),
(9, 'Lead topish', 6);


-- EmployeeTasks
INSERT INTO employee_tasks (id, employee_id, task_id) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 3),
(4, 2, 4),
(5, 3, 5),
(6, 3, 6),
(7, 4, 7),
(8, 5, 8),
(9, 6, 9);
