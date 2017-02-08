
from openerp.report import report_sxw
from openerp import models

class students_info_report_wiz_cla(report_sxw.rml_parse):
    
    _name = 'student.wiz.report'

    def __init__(self, cr, uid, name, context):
        super(students_info_report_wiz_cla, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'line': self.set_context(),
        })
        print "##########################" ,self.set_context
        
        self.context = context
    
    
    def set_context(self,data):
        
        self.cr.execute(''' select * from students ''')
        res = self.cr.dictfetchall()
        return res
    
class school_stu_re_wiz(models.AbstractModel):
    _name = 'report.students.students_info_report_wiz'
    _inherit = 'report.abstract_report'
    _template = 'schoolModul.students_info_report_wiz'
    _wrapped_report_class = students_info_report_wiz_cla



