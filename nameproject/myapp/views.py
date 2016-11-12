from django.shortcuts import render
from .models import grades
#Importamos las librerias de graphos para realizar las estadisticas
from graphos.renderers.morris import BarChart
from graphos.sources.model import SimpleDataSource


def get_grades(request):
<<<<<<< HEAD
    """ Obtenemos el get de nuestro formulario,
        Si no hay datos alimentamos vacio para evitar errores
    """
    student_id = request.GET.get('student_id', '')
    # Validamos nuestra variable
    if student_id:
        # Realizamos nuestra consulta por student_id orden por type
        queryset = grades.objects(student_id=student_id).order_by('type')
        # Creamos Nuestra lista
        scores_chart = [['type', 'score'],]
        # Agregamos valores a nuestra lista
        for grad in queryset:
            scores_chart.append(
                [
                    grad.type,
                    grad.score,
                 ]
            )
        # Esto nos crea nuestra estadistica
        data_source = SimpleDataSource(data=scores_chart)
        donut_chart = BarChart(data_source)
        context = {
            'donut_chart': donut_chart,
            'student_id': student_id
        }
        # Pasamos nuestros datos al template
        return render(request, 'myapp/get_grades.html', context)
    else:
        return render(request, 'myapp/get_grades.html')
=======
    my_grades = grades.objects()
    variable = 888
    context = {
        'my_grades': my_grades
    }
    return render(request, 'myapp/get_grades.html', context)
>>>>>>> parent of 2a4e010... primera prueba se agrega variable
