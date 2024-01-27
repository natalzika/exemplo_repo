from datetime import datetime

def processing_date(payload):
    try:
        hora_atual = datetime.now()
        data_formatada = hora_atual.strftime("%Y%m%d")

        if payload['JobName'] == 'a':
            return str(data_formatada)
        elif payload['JobName'] == 'b':
            lista_formatada = [str(data_formatada)]
            return lista_formatada
        else:
            return f"Payload inválido. Insira a variável JobName de forma correta."
    except Exception as e:
        return f"Exception nao mapeada {e}"

def lambda_handler(event, context):
    formatted_date = processing_date(event)
    context = {
        "anomesdia": formatted_date,
        "status_code": 200
    }
    return context
