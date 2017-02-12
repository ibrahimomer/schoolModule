
from openerp.report import report_sxw
from openerp import models

class courses_info_wiz_cl(report_sxw.rml_parse):
    
    _name = 'course.wiz.report'


    def __init__(self, cr, uid, name, context):


        super(courses_info_wiz_cl, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'line': self.set_context,
        })
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ init"

        #don't enter here i wonder why 

        
        self.context = context
    
    
    def set_context(self,data):
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ set_context "
        self.cr.execute(''' select * from courses ''')
        res = self.cr.dictfetchall()
        return res
    
class cour_wiz(models.AbstractModel):
    _name = 'report.courses.courses_info_wiz'
    _inherit = 'report.abstract_report'
    _template = 'schoolModul.courses_info_wiz'
    _wrapped_report_class = courses_info_wiz_cl
