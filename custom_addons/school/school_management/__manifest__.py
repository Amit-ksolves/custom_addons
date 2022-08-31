{
    'name': 'school_management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'school_management Software',
    'depends': ['base', 'hr'],
    'application': True,

    'data': [
        'security/ir.models.access.csv',
        # 'security/security.xml',
        'views/student_view.xml',
        'views/class_view.xml',
        'views/teacher_view.xml',
        'views/fees_view.xml',
        'views/subjects_view.xml',
        # 'views/random_view.xml',
        'report/report.xml',
        'report/student_details.xml',
        'wizard/exams_view.xml',
    ],
}
