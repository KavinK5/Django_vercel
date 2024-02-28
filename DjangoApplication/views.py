from django.shortcuts import render,redirect,get_object_or_404

from .models import TableCreation

from collections import Counter

def errFunc(req2,user_ID):
    user = get_object_or_404(TableCreation, id= user_ID)
    return render(req2, 'Error Page.html', {'user': user})


def goCourseTab(req3):
    return render(req3,'TableFileHTML.html')

def goHomePage(req):
    if req.method == 'POST':

        NAME_swap = req.POST['Cname']
        FNAME_swap = req.POST['Cdadname']
        GENDER_swap = req.POST['FetchGender']
        #FIRST_3 COLUMNS

        SUBLEVELQUALIF = req.POST['FetchQualification']

        SCHOOL_NAME = req.POST['Cschname']

        DEGREE = req.POST['FetchDegree']
        DEPT = req.POST['FetchDept']

        DIPQUALIF = req.POST['Cdip']

        INSTITUTION = req.POST['Cclgname']

        if True:
            if SUBLEVELQUALIF == 'SSLC' or SUBLEVELQUALIF == 'HSC':
                QUALIF_swap = SUBLEVELQUALIF
                INSTIT_swap = SCHOOL_NAME

            elif SUBLEVELQUALIF == 'Degree':
                QUALIF_swap = DEGREE + ' ' + DEPT
                INSTIT_swap = INSTITUTION

            elif SUBLEVELQUALIF == 'Others':
                QUALIF_swap = DIPQUALIF
                INSTIT_swap = INSTITUTION
        YOPO_swap = req.POST['Cyr']
        YOPO_swap = int(YOPO_swap)
        # COLUMNS 4,5,6

        EMAIL_swap = req.POST['Cem']
        CONTACT_swap = req.POST['Ccntct']



        CONTACT_swap = str(CONTACT_swap)
        CONTACT_swap  = CONTACT_swap.replace('-','')
        CONTACT_swap = int(CONTACT_swap)

        strCONTACT_swap = str(CONTACT_swap)
        if strCONTACT_swap.count('0') >= 5:
            return redirect('Zero')
        # COLUMNS 7,8

        FIELD_swap = req.POST['FetchField']
        COURSES_swap = req.POST['FetchCourse']

                # COLUMNS 9,10

        MODE_swap = req.POST['FetchMode']
        # COLUMN 11

        from datetime import datetime
        now = datetime.now()

        DATE_swap = str(now.strftime('%d')) + ',' + now.strftime('%B') + ' ' + str(now.strftime('%Y'))

        if TableCreation.objects.filter(EmailID_COL = EMAIL_swap).exists():
            return redirect('NameEmailError')

        get = TableCreation.objects.create(Name_COL = NAME_swap,
                                           FathersName_COL = FNAME_swap,
                                           Gender_COL = GENDER_swap,
                                           Qualification_COL = QUALIF_swap,
                                           Institution_COL = INSTIT_swap,
                                           YearOfPassedOut_COL = YOPO_swap,
                                           MobileNumber_COL = CONTACT_swap,
                                           ModeOfClass_COL = MODE_swap,
                                           OptedCourse_COL = COURSES_swap,
                                           EmailID_COL = EMAIL_swap,
                                           OptedField_COL = FIELD_swap,
                                           DateOfEntry_COL = DATE_swap)
        # COLUMN 12

        # viewsTable = TableCreation()
        #
        #
        # viewsTable.Gender_COL = GENDER_swap
        # viewsTable.FathersName_COL = FNAME_swap
        # viewsTable.Name_COL = NAME_swap
        #
        # viewsTable.DateOfEntry_COL = DATE_swap
        # viewsTable.OptedField_COL = FIELD_swap
        #
        # viewsTable.EmailID_COL = EMAIL_swap
        #
        # viewsTable.OptedCourse_COL = COURSES_swap
        #
        # viewsTable.ModeOfClass_COL = MODE_swap
        #
        # viewsTable.MobileNumber_COL = CONTACT_swap
        #
        # viewsTable.YearOfPassedOut_COL = YOPO_swap
        #
        # viewsTable.Institution_COL = INSTIT_swap
        #
        # viewsTable.Qualification_COL = QUALIF_swap
        # #assigned to the respective column
        #
        # viewsTable.save()
        return redirect('Err404',user_ID = get.id)
        #saved the values to the column

    return render(req,'HomeFileHTML.html')



def goZero(req3):
    return render(req3,'Zeroes.html')

def nameEmailErr(Req3):
    return render(Req3,'NameEmailError.html')

def statistics(req):
    get = TableCreation.objects.all()
    listCourses = [itr.OptedCourse_COL for itr in get]
    dict2 = dict(Counter(listCourses))

    # if 'C' not in dict2:
    #     CstoreZeroOrValue = 0
    #
    # elif 'C' in dict2:
    #     CstoreZeroOrValue = dict2['C']

    CstoreZeroOrValue = dict2.get('C', 0)
    KlinstoreZeroOrValue = dict2.get('Kotlin', 0)
    RstoreZeroOrValue = dict2.get('R', 0)
    RubystoreZeroOrValue = dict2.get('Ruby', 0)

    GolstoreZeroOrValue = dict2.get('Golang', 0)
    phpstoreZeroOrValue = dict2.get('php', 0)
    PystoreZeroOrValue = dict2.get('Python', 0)
    JvstoreZeroOrValue = dict2.get('Java', 0)

    HCJstoreZeroOrValue = dict2.get('HTML,CSS,JS', 0)
    TSstoreZeroOrValue = dict2.get('TypeScript', 0)
    CplstoreZeroOrValue = dict2.get('C++', 0)
    CshstoreZeroOrValue = dict2.get('C Sharp', 0)


    JvfsstoreZeroOrValue = dict2.get('Java Full Stack Web Development', 0)
    PyfsstoreZeroOrValue = dict2.get('Python Full Stack Web Development', 0)
    MERNstoreZeroOrValue = dict2.get('MERN Stack', 0)
    FrtendstoreZeroOrValue = dict2.get('Frontend Web Development', 0)


    PandasstoreZeroOrValue = dict2.get('Python Data Science', 0)
    PyDAZeroOrValue = dict2.get('Python Data Analysis', 0)
    PyAIZeroOrValue = dict2.get('Artificial Intelligence', 0)
    PyMLZeroOrValue = dict2.get('Machine Learning', 0)
    PyDLZeroOrValue = dict2.get('Deep Learning', 0)

    AWSstoreZeroOrValue = dict2.get('AWS', 0)
    AzurestoreZeroOrValue = dict2.get('Microsoft Azure', 0)
    GCSstoreZeroOrValue = dict2.get('Google Cloud Services', 0)

    getDict = {'Ccount': CstoreZeroOrValue, 'Cpluscount': CplstoreZeroOrValue, 'Csharpcount': CshstoreZeroOrValue,
               'Pythoncount': PystoreZeroOrValue, 'Javacount': JvstoreZeroOrValue, 'HCJcount': HCJstoreZeroOrValue,
               'TScount': TSstoreZeroOrValue, 'Rcount': RstoreZeroOrValue, 'Phpcount': phpstoreZeroOrValue,
               'Rubycount': RubystoreZeroOrValue, 'Kotlincount': KlinstoreZeroOrValue, 'Golangcount': GolstoreZeroOrValue,

               'Azurecount': AzurestoreZeroOrValue, 'AWScount': AWSstoreZeroOrValue, 'GCScount' : GCSstoreZeroOrValue,

               'Frntcount': FrtendstoreZeroOrValue, 'MERNcount': MERNstoreZeroOrValue,
               'Pyfscount': PyfsstoreZeroOrValue,
               'Jvfscount': JvfsstoreZeroOrValue,

               'DataSccount': PandasstoreZeroOrValue,'PydeepLcount': PyDLZeroOrValue,
               'MLcount': PyMLZeroOrValue,'AIcount': PyAIZeroOrValue,
               'DataAncount': PyDAZeroOrValue
               }

    totalAdmits = [itr for itr in getDict.values()]
    totalAdmitsCount = sum(totalAdmits)

    getDict['totalAdmitsCount'] = totalAdmitsCount
    return render(req,'Statistics.html',getDict)

def statistics1(req):
    get = TableCreation.objects.all()
    listCourses = [itr.OptedCourse_COL for itr in get]
    dict2 = dict(Counter(listCourses))

    # if 'C' not in dict2:
    #     CstoreZeroOrValue = 0
    #
    # elif 'C' in dict2:
    #     CstoreZeroOrValue = dict2['C']

    CstoreZeroOrValue = dict2.get('C', 0)
    KlinstoreZeroOrValue = dict2.get('Kotlin', 0)
    RstoreZeroOrValue = dict2.get('R', 0)
    RubystoreZeroOrValue = dict2.get('Ruby', 0)

    GolstoreZeroOrValue = dict2.get('Golang', 0)
    phpstoreZeroOrValue = dict2.get('php', 0)
    PystoreZeroOrValue = dict2.get('Python', 0)
    JvstoreZeroOrValue = dict2.get('Java', 0)

    HCJstoreZeroOrValue = dict2.get('HTML,CSS,JS', 0)
    TSstoreZeroOrValue = dict2.get('TypeScript', 0)
    CplstoreZeroOrValue = dict2.get('C++', 0)
    CshstoreZeroOrValue = dict2.get('C Sharp', 0)

    JvfsstoreZeroOrValue = dict2.get('Java Full Stack Web Development', 0)
    PyfsstoreZeroOrValue = dict2.get('Python Full Stack Web Development', 0)
    MERNstoreZeroOrValue = dict2.get('MERN Stack', 0)
    FrtendstoreZeroOrValue = dict2.get('Frontend Web Development', 0)

    PandasstoreZeroOrValue = dict2.get('Python Data Science', 0)
    PyDAZeroOrValue = dict2.get('Python Data Analysis', 0)
    PyAIZeroOrValue = dict2.get('Artificial Intelligence', 0)
    PyMLZeroOrValue = dict2.get('Machine Learning', 0)
    PyDLZeroOrValue = dict2.get('Deep Learning', 0)

    AWSstoreZeroOrValue = dict2.get('AWS', 0)
    AzurestoreZeroOrValue = dict2.get('Microsoft Azure', 0)

    getDict = {'Ccount': CstoreZeroOrValue, 'Cpluscount': CplstoreZeroOrValue, 'Csharpcount': CshstoreZeroOrValue,
               'Pythoncount': PystoreZeroOrValue, 'Javacount': JvstoreZeroOrValue, 'HCJcount': HCJstoreZeroOrValue,
               'TScount': TSstoreZeroOrValue, 'Rcount': RstoreZeroOrValue, 'Phpcount': phpstoreZeroOrValue,
               'Rubycount': RubystoreZeroOrValue, 'Kotlincount': KlinstoreZeroOrValue,
               'Golangcount': GolstoreZeroOrValue,

               'Azurecount': AzurestoreZeroOrValue, 'AWScount': AWSstoreZeroOrValue,

               'Frntcount': FrtendstoreZeroOrValue, 'MERNcount': MERNstoreZeroOrValue,
               'Pyfscount': PyfsstoreZeroOrValue,
               'Jvfscount': JvfsstoreZeroOrValue,

               'DataSccount': PandasstoreZeroOrValue,'PydeepLcount': PyDLZeroOrValue,
               'MLcount': PyMLZeroOrValue,'AIcount': PyAIZeroOrValue,
               'DataAncount': PyDAZeroOrValue
               }

    totalAdmits = [itr for itr in getDict.values()]
    totalAdmitsCount = sum(totalAdmits)

    getDict['totalAdmitsCount'] = totalAdmitsCount
    return render(req,'Statistics2.html',getDict)