# install.packages(c("tidyverse", "ggplot2"))
library(tidyverse)

# Limpiar entorno
rm(list = ls())

# Cargar datos
datos <- read.csv("C:/Users/isall/OneDrive/UNI/TFG/TFG/datos.csv", stringsAsFactors = FALSE)

# Eliminar columnas completamente vacías
datos <- datos[, colSums(!is.na(datos)) > 0]

# Convertir variables a factores ordenados donde sea necesario
datos$pregunta_23 <- factor(datos$pregunta_23, levels = c("Muy baja", "Baja", "Media", "Alta", "Muy alta"), ordered = TRUE)
datos$pregunta_22 <- factor(datos$pregunta_22)
datos$pregunta_16 <- factor(datos$pregunta_16, levels = c("Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"), ordered = TRUE)
datos$pregunta_17 <- factor(datos$pregunta_17, levels = c("Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"), ordered = TRUE)
datos$pregunta_18 <- factor(datos$pregunta_18, levels = c("Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"), ordered = TRUE)

colores_confianza <- c(
    "Muy baja" = "#49006a",
    "Baja"     = "#2b8cbe",
    "Media"    = "#66c2a4",
    "Alta"     = "#ffff33"
)




#Orden respuesta
mutate(pregunta_23 = factor(pregunta_23, levels = c("Muy baja", "Baja", "Media", "Alta", "Muy alta")))

grafico_p23 <- datos %>%
  count(pregunta_23, name = "n") %>%
  mutate(
    porcentaje = round(n / sum(n) * 100, 1),
    pregunta_23 = factor(pregunta_23, levels = c("Muy baja", "Baja", "Media", "Alta", "Muy alta"))
  ) %>%
  ggplot(aes(x = pregunta_23, y = porcentaje, fill = pregunta_23)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  labs(
    title = "Nivel de confianza en los sistemas de IA",
    x = NULL,
    y = "Porcentaje",
    fill = "Confianza"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    axis.title.y = element_text(size = 15),
    legend.text = element_text(size = 15),
    legend.title = element_text(size = 14),
    plot.title = element_text(hjust = 0.5, face = "bold", size = 16)
  )

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/pregunta_23_resultado.png", grafico_p23, width = 12, height = 7, dpi = 400)

## Gráfica nivel conocimiento IA --> nivel confianzaz
datos$pregunta_22 <- recode(datos$pregunta_22,
  "Sí, cuanto más sé, más confianza tengo" = "Sí, cuanto más sé,\nmás confianza tengo", 
  "Sí, cuanto más sé, más desconfío" = "Sí, cuanto más sé,\nmás desconfío", 
  "No, mi opinión no depende de lo que sepa sobre ella" = "No, mi opinión no depende\nde lo que sepa sobre ella"
)


colores_p22 <- c(
  "Sí, cuanto más sé,\nmás confianza tengo" = "#4b62a6",
  "Sí, cuanto más sé,\nmás desconfío"       = "#2b8cbe",
  "No, mi opinión no depende\nde lo que sepa sobre ella" = "#66c2a4"
)


#Orden respuesta
mutate(pregunta_22 = factor(pregunta_22, levels = c("No, mi opinión no depende\nde lo que sepa sobre ella", "Sí, cuanto más sé,\nmás desconfío", "Sí, cuanto más sé,\nmás confianza tengo")))

grafico_p22 <- datos %>%
  count(pregunta_22, name = "n") %>%
  mutate(
    porcentaje = round(n / sum(n) * 100, 1),
  ) %>%
  ggplot(aes(x = pregunta_22, y = porcentaje, fill = pregunta_22)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  scale_fill_manual(values = colores_p22) +
  labs(
    title = "Nivel de confianza en los sistemas de IA en función del conocimiento",
    x = NULL,
    y = "Porcentaje",
    fill = "Confianza"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    axis.title.y = element_text(size = 15),
    legend.text = element_text(size = 15),
    legend.title = element_text(size = 14),
    plot.title = element_text(hjust = 0.5, face = "bold", size = 16)
  )

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/pregunta_22_resultado.png", grafico_p22, width = 12, height = 7, dpi = 400)

# Filtrar datos: excluir No binario y edades con muy pocos casos
datos_filtrados <- datos %>%
  filter(
    genero != "No binario",
    !(edad %in% c("35 - 44", "Prefiero no decirlo", "Mayor de 64"))
  )

datos_filtrados$pregunta_23 <- factor(
  datos_filtrados$pregunta_23,
  levels = rev(c("Muy baja", "Baja", "Media", "Alta", "Muy alta")),
  ordered = TRUE
)

# Gráfico: Confianza por Género
grafico_genero <- ggplot(datos_filtrados, aes(x = genero, fill = pregunta_23)) +
  geom_bar(position = "fill") +
  scale_fill_manual(values = colores_confianza) +
  labs(
    title = "Confianza en la IA por Género",
    y = "Proporción",
    x = "Género",
    fill = "Confianza"
  ) +
  theme_minimal(base_size = 16) +
  theme(
    plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 11),
    legend.title = element_text(size = 11),
    legend.text = element_text(size = 11)
  )


ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/confianza_genero.png",
  plot = grafico_genero,
  width = 6,
  height = 5,
  dpi = 300
)


# Gráfico: Confianza por Edad (excluyendo grupos con pocas respuestas)
grafico_edad <- datos_filtrados %>%
  filter(!(edad %in% c("35 - 44", "45 - 54", "Prefiero no decirlo", "Mayor de 64"))) %>%
  ggplot(aes(x = edad, fill = pregunta_23)) +
  geom_bar(position = "fill") +
  scale_fill_manual(values = colores_confianza) +
  labs(
    title = "Confianza en la IA por Edad",
    y = "Proporción",
    x = "Edad",
    fill = "Confianza"
  ) +
  theme_minimal(base_size = 16) +
  theme(
    plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 11),
    legend.title = element_text(size = 11),
    legend.text = element_text(size = 11)
  )


ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/confianza_edad.png",
  plot = grafico_edad,
  width = 7,
  height = 5,
  dpi = 300
)


datos$pregunta_2 <- factor(datos$pregunta_2, levels = c(
  "Nunca", "Sí, esporádicamente", "Sí, mensualmente", "Sí, semanalmente", "Sí, diariamente"
), ordered = TRUE)

datos$edad <- factor(datos$edad, levels = c(
  "18 - 24", "25 - 34", "55 - 64"
), ordered = TRUE)

# Eliminar edades con pocas respuestas para mejor visualización
datos_uso_filtrado <- datos %>%
  filter(
    !(edad %in% c("35 - 44", "45 - 54", "Prefiero no decirlo", "Mayor de 64")),
    !is.na(edad),
    !is.na(pregunta_2)
  )

colores_uso_ia <- c(
  "Nunca" = "#49006a",
  "Sí, esporádicamente" = "#4b62a6",
  "Sí, mensualmente" = "#2b8cbe",
  "Sí, semanalmente" = "#66c2a4",
  "Sí, diariamente" = "#ffff33"
)

grafico_uso_edad <- ggplot(datos_uso_filtrado, aes(x = edad, fill = pregunta_2)) +
  geom_bar(position = "fill") +
  scale_fill_manual(values = colores_uso_ia) +  # <-- esta línea
  labs(
    title = "Frecuencia de uso de IA según la edad",
    x = "Edad",
    y = "Proporción",
    fill = "Frecuencia de uso"
  ) +
  theme_minimal(base_size = 16) +
  theme(
    plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 11),
    legend.title = element_text(size = 11),
    legend.text = element_text(size = 11)
  )

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/uso_IA_por_edad.png",
  plot = grafico_uso_edad,
  width = 7,
  height = 5,
  dpi = 500
)

# Prueba estadística: chi-cuadrado entre edad y uso de IA
tabla_edad_uso <- table(datos_uso_filtrado$edad, datos_uso_filtrado$pregunta_2)
chisq.test(tabla_edad_uso)

# Codificar confianza (pregunta_23) como valores numéricos
datos$confianza_num <- as.numeric(factor(
  datos$pregunta_23,
  levels = c("Muy baja", "Baja", "Media", "Alta", "Muy alta"),
  ordered = TRUE
))

# Codificar uso de IA (pregunta_2) como valores numéricos
datos$uso_ia_num <- as.numeric(factor(
  datos$pregunta_2,
  levels = c("Nunca", "Sí, esporádicamente", "Sí, mensualmente", "Sí, semanalmente", "Sí, diariamente"),
  ordered = TRUE
))

# Filtrar valores completos
correlacion_datos <- datos %>%
  filter(!is.na(confianza_num), !is.na(uso_ia_num))

# Calcular coeficiente de correlación de Spearman
cor.test(correlacion_datos$uso_ia_num, correlacion_datos$confianza_num, method = "spearman")


################### Análisis 2: Decisiones delegadas a la IA (gráfico C)

# Separar respuestas múltiples
decision_split <- datos %>%
  separate_rows(pregunta_21, sep = ",") %>%
  mutate(pregunta_21 = str_trim(pregunta_21)) %>%  # Elimina espacios
  filter(!is.na(pregunta_21) & pregunta_21 != "") %>%
  mutate(pregunta_21 = str_remove_all(pregunta_21, "\\[|\\]|\""))  # Limpia corchetes y comillas

# Agrupar por categoría y contar
resumen_categorias <- decision_split %>%
  count(pregunta_21, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  arrange(desc(n))

print(resumen_categorias)


decision_split <- datos %>%
  separate_rows(pregunta_21, sep = ",") %>%
  mutate(pregunta_21 = str_trim(pregunta_21)) %>%
  filter(!is.na(pregunta_21) & pregunta_21 != "") %>%
  mutate(pregunta_21 = str_remove_all(pregunta_21, "\\[|\\]|\""))

# Reemplazar etiquetas largas con saltos de línea
decision_split$pregunta_21 <- recode(decision_split$pregunta_21,
  "Decisiones éticas en situaciones límite (como en coches autónomos)" = "Decisiones éticas en\nsituaciones límite", 
  "Decisiones legales o judiciales" = "Decisiones legales\no judiciales"
)

# Agrupar y contar
resumen_categorias <- decision_split %>%
  count(pregunta_21, name = "n") %>%
  arrange(desc(n))

# Crear gráfico con SOLO el número
grafico_categorias <- ggplot(resumen_categorias, aes(x = reorder(pregunta_21, n), y = n)) +
  geom_col(fill = "#66c2a4") +
  geom_text(aes(label = n), hjust = -0.1, size = 5) +
  coord_flip() +
  labs(
    title = "Frecuencia de decisiones delegadas a la IA",
    x = "Tipo de decisión",
    y = "Número de personas"
  ) +
  theme_minimal(base_size = 17) +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 16),
    axis.text = element_text(size = 16)
  )

# Guardar el gráfico
ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/decisiones_delegadas_limpio.jpg",
  plot = grafico_categorias,
  width = 10,
  height = 6,
  dpi = 450,
  device = "jpeg"
)


############## Gráficos D + E
datos$pregunta_19 <- factor(datos$pregunta_19, levels = c(
  "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
), ordered = TRUE)

datos$pregunta_20 <- factor(datos$pregunta_20, levels = c(
  "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
), ordered = TRUE)

# Calcular frecuencias
frecuencias_p19 <- datos %>%
  count(pregunta_19)


g_pregunta_19 <- ggplot(frecuencias_p19, aes(x = pregunta_19, y = n)) +
  geom_col(fill = "#2b8cbe") +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  labs(
    title = "Opinión sobre el impacto actual de la IA",
    x = "Nivel de acuerdo",
    y = "Número de respuestas"
  ) +
  theme_minimal(base_size = 17) +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 16),
    axis.text = element_text(size = 16),
    legend.title = element_text(size = 16),
    legend.text = element_text(size = 16)
  )


ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/pregunta_19.jpg",
  plot = g_pregunta_19,
  width = 10,      
  height = 5.8,     
  dpi = 400,        
  device = "jpeg"   
)

# Calcular frecuencias
frecuencias_p20 <- datos %>%
  count(pregunta_20)


g_pregunta_20 <- ggplot(frecuencias_p20, aes(x = pregunta_20, y = n)) +
  geom_col(fill = "#66c2a4") +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  labs(
    title = "Opinión sobre el impacto futuro de la IA",
    x = "Nivel de acuerdo",
    y = "Número de respuestas"
  ) +
  theme_minimal(base_size = 17) +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 16),
    axis.text = element_text(size = 16)
  )

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/pregunta_20.jpg",
  plot = g_pregunta_20,
  width = 10,
  height = 5.8,
  dpi = 400,
  device = "jpeg"
)


########################### Gráficos F + E + G : Percepción sobre sesgos en IA y humanos

# Pregunta 5: ¿Crees que la IA toma decisiones sesgadas?
datos$pregunta_5 <- factor(datos$pregunta_5)

datos$pregunta_5 <- recode(datos$pregunta_5,
  "Sí, porque aprenden de datos que pueden estar sesgados por la sociedad" = "Sí, porque aprenden de datos\nque pueden estar sesgados\npor la sociedad", 
  "No, porque la IA analiza los datos de forma neutral" = "No, porque la IA analiza\nlos datos de forma neutral", 
  "No estoy seguro/a" = "No estoy seguro/a"
)
colores_p5 <- c(
  "Sí, porque aprenden de datos\nque pueden estar sesgados\npor la sociedad" = "#2b8cbe",
  "No, porque la IA analiza\nlos datos de forma neutral" = "#66c2a4",
  "No estoy seguro/a" = "#ffff33"
)

grafico_p5 <- datos %>% 
  count(pregunta_5, name = "n") %>%
  ggplot(aes(x = reorder(pregunta_5, -n), y = n, fill = pregunta_5)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +  # Solo recuento
  scale_fill_manual(values = colores_p5) +
  labs(
    title = "Sesgos en la IA en la toma de decisiones",
    x = "Respuesta",
    y = "Número de respuestas",
    fill = "Respuesta"
  ) +
  theme_minimal(base_size = 18) +
  theme(
    axis.text.x = element_blank(),
    axis.title.x = element_blank(),
    axis.ticks.x = element_blank(),
    plot.title = element_text(hjust = 0.5, face = "bold")
  )

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/grafica_F_sesgos_IA.jpg",
  plot = grafico_p5,
  width = 12, height = 6, dpi = 450
)


# Pregunta 6: ¿Las personas tienen sesgos?
datos$pregunta_6 <- factor(datos$pregunta_6)

datos$pregunta_6 <- recode(datos$pregunta_6,
"Sí, siempre tenemos algún tipo de sesgo" = "Sí, siempre tenemos\nalgún tipo de sesgo", 
"A menudo, en función del contexto" = "En función del contexto", 
"No, las personas podemos decidir de forma totalmente objetiva" = "No, las personas\npodemos decidir de forma\ntotalmente objetiva"
)

colores_p6 <- c(
  "Sí, siempre tenemos\nalgún tipo de sesgo" = "#2b8cbe",
  "En función del contexto" = "#66c2a4",
  "No, las personas\npodemos decidir de forma\ntotalmente objetiva" = "#ffff33"
)

grafico_p6 <- datos %>%
  count(pregunta_6, name = "n") %>%
  ggplot(aes(x = reorder(pregunta_6, -n), y = n, fill = pregunta_6)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +  # Solo recuento
  scale_fill_manual(values = colores_p6) +
  labs(
    title = "Sesgos en las personas en la\ntoma de decisiones",
    x = "Respuesta",
    y = "Número de respuestas",
    fill = "Respuesta"
  ) +
  theme_minimal(base_size = 18) +
  theme(
    axis.text.x = element_blank(),
    axis.title.x = element_blank(),
    axis.ticks.x = element_blank(),
    plot.title = element_text(hjust = 0.5, face = "bold")
  )

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/grafica_E_sesgos_humanos.jpg",
  plot = grafico_p6,
  width = 12, height = 6, dpi = 450
)

### Gráficas en relacion con la regulación de la IA
datos$pregunta_8 <- factor(datos$pregunta_8)
datos$pregunta_9 <- factor(datos$pregunta_9)

## Gráfico confianza IA + quién tiene más sesgos

datos$pregunta_7 <- factor(datos$pregunta_7, levels = c("Una persona", "Un sistema con IA"))
datos$pregunta_23 <- factor(datos$pregunta_23, levels = c("Muy baja", "Baja", "Media", "Alta", "Muy alta"), ordered = TRUE)


colores_confianza <- c(
    "Muy baja" = "#49006a",
    "Baja"     = "#2b8cbe",
    "Media"    = "#66c2a4",
    "Alta"     = "#ffff33"
)

grafico_confianza_vs_sesgos <- datos %>%
  filter(!is.na(pregunta_7), !is.na(pregunta_23)) %>%
  ggplot(aes(x = pregunta_7, fill = pregunta_23)) +
  geom_bar(position = "fill") +
  scale_fill_manual(values = colores_confianza) +
  labs(
    title = "Nivel de confianza en la IA según atribución de sesgos",
    x = "¿Quién tiene más sesgos?",
    y = "Proporción",
    fill = "Confianza en la IA"
  ) +
  theme_minimal(base_size = 16) +
  theme(
    plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 11),
    legend.title = element_text(size = 11),
    legend.text = element_text(size = 11)
  )

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/confianza_vs_sesgos.png",
  plot = grafico_confianza_vs_sesgos,
  width = 6.5,
  height = 5,
  dpi = 350
)

## Gráfica Uso IA + sesgos 

datos$pregunta_7 <- factor(datos$pregunta_7, levels = c("Una persona", "Un sistema con IA"))

datos$pregunta_2 <- factor(datos$pregunta_2, levels = c(
  "Nunca", 
  "Sí, esporádicamente", 
  "Sí, mensualmente", 
  "Sí, semanalmente", 
  "Sí, diariamente"
), ordered = TRUE)


colores_uso_ia <- c(
  "Nunca" = "#49006a",
  "Sí, esporádicamente" = "#4b62a6",
  "Sí, mensualmente" = "#2b8cbe",
  "Sí, semanalmente" = "#66c2a4",
  "Sí, diariamente" = "#ffff33"
)

grafico_uso_vs_sesgos <- datos %>%
  filter(!is.na(pregunta_7), !is.na(pregunta_2)) %>%
  ggplot(aes(x = pregunta_7, fill = pregunta_2)) +
  geom_bar(position = "fill") +
  scale_fill_manual(values = colores_uso_ia) +
  labs(
    title = "Frecuencia de uso de IA según atribución de sesgos",
    x = "¿Quién tiene más sesgos?",
    y = "Proporción",
    fill = "Uso de IA"
  ) +
  theme_minimal(base_size = 16) +
  theme(
    plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 11),
    legend.title = element_text(size = 11),
    legend.text = element_text(size = 11)
  )

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/uso_vs_sesgos.png",
  plot = grafico_uso_vs_sesgos,
  width = 7,
  height = 5,
  dpi = 350
)

# Crear un vector de colores personalizados
colores_p8 <- c(
  "Las empresas que desarrollan los algoritmos" = "#4b62a6",  
  "Los gobiernos y organismos reguladores" = "#2b8cbe",
  "Los usuarios, que deben usar la IA de forma crítica" = "#66c2a4",
  "Todos los anteriores comparten responsabilidad" = "#ffff33"
)
# Gráfico: Responsable de evitar sesgos (solo número de respuestas)
grafico_p8 <- datos %>%
  count(pregunta_8, name = "n") %>%
  ggplot(aes(x = reorder(pregunta_8, -n), y = n, fill = pregunta_8)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +  # Mostrar solo el número
  scale_fill_manual(values = colores_p8) +
  labs(
    title = "¿Quién debería evitar los sesgos en la IA?",
    x = NULL,
    y = "Número de respuestas",
    fill = "Responsable"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_blank(),
    axis.ticks.x = element_blank(),
    plot.title = element_text(hjust = 0.5, face = "bold")
  )

# Guardar gráfico
ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/responsable_sesgos_IA.png",
  plot = grafico_p8,
  width = 10,
  height = 5,
  dpi = 450
)


#######
niveles_p9 <- c(
  "Educación primaria/secundaria",
  "Universidad",
  "En el ámbito laboral",
  "No creo que sea necesario\nregular ni concienciar\nsobre la IA"
)

datos$pregunta_9 <- recode(datos$pregunta_9,
  "En la educación primaria y secundaria (colegios)" = "Educación primaria/secundaria",
  "En la universidad" = "Universidad", 
  "En el ámbito laboral" = "En el ámbito laboral", 
  "No creo que sea necesario regular ni concienciar sobre la IA" = "No creo que sea necesario\nregular ni concienciar\nsobre la IA"
)

datos$pregunta_9 <- factor(datos$pregunta_9, levels = niveles_p9)

base_p9 <- tibble(pregunta_9 = factor(niveles_p9, levels = niveles_p9)) %>%
  left_join(
    datos %>%
      count(pregunta_9, name = "n"),
    by = "pregunta_9"
  ) %>%
  mutate(n = replace_na(n, 0)) 


colores_p9 <- c(
  "Educación primaria/secundaria" = "#4b62a6",
  "Universidad" = "#2b8cbe",
  "En el ámbito laboral" = "#66c2a4",
  "No creo que sea necesario\nregular ni concienciar\nsobre la IA" = "#ffff33"
)

grafico_p9 <- ggplot(base_p9, aes(x = reorder(pregunta_9, -n), y = n, fill = pregunta_9)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  scale_fill_manual(values = colores_p9, drop = FALSE) +
  labs(
    title = "Etapa clave para educar sobre la IA",
    x = NULL,
    y = "Número de respuestas",
    fill = "Etapa educativa"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_blank(),
    axis.ticks.x = element_blank(),
    plot.title = element_text(hjust = 0.5, face = "bold")
  )

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/educacion_sobre_IA.png",
  plot = grafico_p9,
  width = 10,
  height = 5,
  dpi = 450
)

##### Gráfica principios éticos
datos$pregunta_16 <- factor(datos$pregunta_16, levels = c(
  "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
), ordered = TRUE)

datos$pregunta_17 <- factor(datos$pregunta_17, levels = c(
  "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
), ordered = TRUE)

datos$pregunta_18 <- factor(datos$pregunta_18, levels = c(
  "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
), ordered = TRUE)


principio_16 <- datos %>%
  count(pregunta_16, name = "n") %>%
  mutate(pregunta = "Dignidad humana", nivel = pregunta_16) %>%
  select(pregunta, nivel, n)

principio_17 <- datos %>%
  count(pregunta_17, name = "n") %>%
  mutate(pregunta = "Libertad", nivel = pregunta_17) %>%
  select(pregunta, nivel, n)

principio_18 <- datos %>%
  count(pregunta_18, name = "n") %>%
  mutate(pregunta = "Justicia social", nivel = pregunta_18) %>%
  select(pregunta, nivel, n)

# Unir todo
resumen_principios <- bind_rows(principio_16, principio_17, principio_18)

print(resumen_principios)

colores_principios <- c(
  "Totalmente desacuerdo" = "#49006a",
  "Desacuerdo" = "#4b62a6",
  "Neutral" = "#2b8cbe",
  "Acuerdo" = "#66c2a4",
  "Totalmente acuerdo" = "#ffff33"
)

principios <- ggplot(resumen_principios, aes(x = pregunta, y = n, fill = nivel)) +
  geom_col(position = "fill") +
  scale_fill_manual(values = colores_principios) +
  labs(
    title = "Nivel de acuerdo con principios éticos de la IA",
    x = "Principio ético",
    y = "Proporción de respuestas",
    fill = "Nivel de acuerdo"
  ) +
  theme_minimal(base_size = 16) +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5)
  )

# Guardar gráfico
ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/principios.png",
  plot = principios,
  width = 9,
  height = 6,
  dpi = 400
)

##########################################################################

colores_caso1 <- c(
  "Jake Moffatt" = "#4b62a6",      
  "La empresa Air Canada" = "#66c2a4"
)
################ CASO 1
grafico_p10 <- datos %>%
  count(pregunta_10, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_10, -porcentaje), y = porcentaje, fill = pregunta_10)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  scale_fill_manual(values = colores_caso1) +
  labs(
    title = "¿Quién crees que tenía\nrazón en este caso? (Caso 1)",
    x = NULL,
    y = "Porcentaje",
    fill = "Respuesta"
  ) +
  theme_minimal(base_size = 15) +
  theme(
    axis.text.x = element_text(size = 16),   # Texto del eje X
    axis.text.y = element_text(size = 16),   # Texto del eje Y
    axis.title.y = element_text(size = 16),  # Título del eje Y
    legend.text = element_text(size = 16),   # Texto de la leyenda
    legend.title = element_text(size = 15),  # Título de la leyenda
    plot.title = element_text(hjust = 0.5, face = "bold", size = 16)
  )

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/pregunta_caso_1.png", grafico_p10, width = 10, height = 7, dpi = 440)


################ CASO 2
datos$pregunta_13 <- recode(datos$pregunta_13,
  "El joven estadounidense de 17 años" = "Joven\nestadounidense\nde 17 años", 
  "La empresa desarrolladora de la IA." = "Empresa desarrolladora\nde la IA", 
  "El entorno del joven (familiares, escuela, amigos, etc.)" = "Entorno del joven"
)

# Colores consistentes
colores_caso2 <- c(
  "Joven\nestadounidense\nde 17 años" = "#4b62a6",       
  "Empresa desarrolladora\nde la IA" = "#2b8cbe",        
  "Entorno del joven" = "#66c2a4"
)

# Gráfico actualizado
grafico_p13 <- datos %>%
  count(pregunta_13, name = "n") %>%
  ggplot(aes(x = pregunta_13, y = n, fill = pregunta_13)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  scale_fill_manual(values = colores_caso2) +
  labs(
    title = "¿Quién tiene mayor responsabilidad? (Caso 2)",
    x = NULL,
    y = "Número de respuestas",
    fill = "Responsable"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    axis.title.y = element_text(size = 15),
    legend.text = element_text(size = 13),
    legend.title = element_text(size = 14),
    plot.title = element_text(hjust = 0.5, face = "bold", size = 16)
  )

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/pregunta_caso_2.png", grafico_p13, width = 10, height = 6, dpi = 450)

################ CASO 3

datos$pregunta_14 <- recode(datos$pregunta_14,
  "El hombre que mantenía la conversación" = "Hombre que\nmantenia la\nconversación",
  "La empresa responsable del chatbot" = "Empresa\nresponsable\ndel chatbot",
  "La plataforma (Chai) que permitió la interacción" = "Plataforma\nque permitió\nla iterracción"
)

colores_caso3 <- c(
  "Hombre que\nmantenia la\nconversación" = "#4b62a6",       
  "Empresa\nresponsable\ndel chatbot" = "#2b8cbe",        
  "Plataforma\nque permitió\nla iterracción" = "#66c2a4"
)

grafico_p14 <- datos %>%
  count(pregunta_14, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_14, -porcentaje), y = porcentaje, fill = pregunta_14)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  scale_fill_manual(values = colores_caso3) +
  labs(
    title = "¿Quién consideras más responsable? (Caso 3)",
    x = NULL,
    y = "Porcentaje",
    fill = "Responsable"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_text(size = 14),   # Texto del eje X
    axis.text.y = element_text(size = 14),   # Texto del eje Y
    axis.title.y = element_text(size = 15),  # Título del eje Y
    legend.text = element_text(size = 13),   # Texto de la leyenda
    legend.title = element_text(size = 14),  # Título de la leyenda
    plot.title = element_text(hjust = 0.5, face = "bold", size = 16)
  )

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/pregunta_caso_3.png", grafico_p14, width = 10, height = 6, dpi = 450)



datos$pregunta_12 <- recode(datos$pregunta_12,
  "No, deberían estar restringidas por edad" = "No, deberían estar\nrestringidas por edad ",
  "Sí, siempre que el usuario acepte los términos de uso" = "Sí, siempre que el\nusuario acepte los\ntérminos de uso",
  "Deberían estar etiquetadas con advertencias sobre su contenido" = "Deberían estar etiquetadas\ncon advertencias sobre\nsu contenido"
)

colores_p12 <- c(
  "No, deberían estar\nrestringidas por edad " = "#4b62a6",       
  "Sí, siempre que el\nusuario acepte los\ntérminos de uso" = "#2b8cbe",        
  "Deberían estar etiquetadas\ncon advertencias sobre\nsu contenido" = "#66c2a4"
)

grafico_p12 <- datos %>%
  count(pregunta_12, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_12, -porcentaje), y = porcentaje, fill = pregunta_12)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  scale_fill_manual(values = colores_p12) +
  labs(
    title = "¿Las IAs emocionales deberían estar disponibles para cualquier usuario?",
    x = NULL,
    y = "Porcentaje",
    fill = "Respuesta"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_text(size = 14),   # Texto del eje X
    axis.text.y = element_text(size = 14),   # Texto del eje Y
    axis.title.y = element_text(size = 15),  # Título del eje Y
    legend.text = element_text(size = 15),   # Texto de la leyenda
    legend.title = element_text(size = 14),  # Título de la leyenda
    plot.title = element_text(hjust = 0.5, face = "bold", size = 16)
  )

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/pregunta_12_resultado.png", grafico_p12, width = 12, height = 7, dpi = 400)

datos$pregunta_15 <- recode(datos$pregunta_15,
  "Sí, debería ser un requisito mínimo" = "Sí, debería ser un\nrequisito mínimo", 
  "No, la responsabilidad final siempre debería recaer en el usuario" = "No, la responsabilidad final\nsiempre debería recaer\nen el usuario", 
  "Depende del tipo de IA y su finalidad" = "Depende del tipo de IA\ny su finalidad"
)

colores_p15 <- c(
  "Sí, debería ser un\nrequisito mínimo" = "#4b62a6",       
  "No, la responsabilidad final\nsiempre debería recaer\nen el usuario" = "#2b8cbe",        
  "Depende del tipo de IA\ny su finalidad" = "#66c2a4"
)

grafico_p15 <- datos %>%
  count(pregunta_15, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_15, -porcentaje), y = porcentaje, fill = pregunta_15)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  scale_fill_manual(values = colores_p15) +
  labs(
    title = "¿La IA conversacional debería detectar crisis emocionales?",
    x = NULL,
    y = "Porcentaje",
    fill = "Respuesta"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_text(size = 14),   # Texto del eje X
    axis.text.y = element_text(size = 14),   # Texto del eje Y
    axis.title.y = element_text(size = 15),  # Título del eje Y
    legend.text = element_text(size = 15),   # Texto de la leyenda
    legend.title = element_text(size = 14),  # Título de la leyenda
    plot.title = element_text(hjust = 0.5, face = "bold", size = 16)
  )

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/Analisis/pregunta_15_resultado.png", grafico_p15, width = 12, height = 7, dpi = 400)


