import csv
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('C:/Users/resid/GitHub/ProyectoFinalTallerIntegrado/db.sqlite3')
cursor = conn.cursor()

# Abrir el archivo CSV
with open('C:/Users/resid/GitHub/ProyectoFinalTallerIntegrado/dataset_updated.csv', newline='') as csvfile:
  reader = csv.reader(csvfile)

  # Saltar la fila del encabezado (opcional, si el CSV tiene encabezados)
  next(reader)

  # Crear la consulta para insertar datos en la tabla
  insert_query = '''
  INSERT INTO streamers_streamer (
      name,
      language,
      type,
      most_streamed_game,
      average_stream_duration,
      followers_gained_per_stream,
      avg_viewers_per_stream,
      avg_games_per_stream,
      total_time_streamed,
      total_followers,
      total_views,
      total_games_streamed,
      active_days_per_week,
      most_active_day,
      day_with_most_followers_gained
  ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  '''

  # Insertar cada fila del CSV en la tabla
  for row in reader:
    cursor.execute(insert_query, row)

# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión
conn.close()

print("Datos importados exitosamente!")