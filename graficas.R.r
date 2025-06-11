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

#Orden resspuesta
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

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_23_resultado.png", grafico_p23, width = 12, height = 7, dpi = 400)

## Gráfica nivel conocimiento IA --> nivel confianzaz
datos$pregunta_22 <- recode(datos$pregunta_22,
  "Sí, cuanto más sé, más confianza tengo" = "Sí, cuanto más sé,\nmás confianza tengo", 
  "Sí, cuanto más sé, más desconfío" = "Sí, cuanto más sé,\nmás desconfío", 
  "No, mi opinión no depende de lo que sepa sobre ella" = "No, mi opinión no depende\nde lo que sepa sobre ella"
)


colores_p22 <- c(
  "Sí, cuanto más sé,\nmás confianza tengo" = "#2b8cbe",
  "Sí, cuanto más sé,\nmás desconfío"       = "#66c2a4",
  "No, mi opinión no depende\nde lo que sepa sobre ella" = "#ffff33"
)


#Orden resspuesta
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

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_22_resultado.png", grafico_p22, width = 12, height = 7, dpi = 400)



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
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/confianza_genero.png",
  plot = grafico_genero,
  width = 6,
  height = 5,
  dpi = 300
)

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
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/confianza_edad.png",
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
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/uso_IA_por_edad.png",
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

library(tidyverse)

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

# Mostrar tabla
print(resumen_categorias)

# Reemplazar etiquetas largas por nombres más cortos
resumen_categorias <- resumen_categorias %>%
  mutate(pregunta_21 = case_when(
    pregunta_21 == "Decisiones éticas en situaciones límite (como en coches autónomos)" ~ "Decisiones éticas en situaciones límite",
    TRUE ~ pregunta_21
  ))

# Gráfico actualizado
grafico_categorias <- ggplot(resumen_categorias, aes(x = reorder(pregunta_21, n), y = n)) +
  geom_col(fill = "#66c2a5") +
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
    axis.text = element_text(size = 16),
    legend.title = element_text(size = 16),
    legend.text = element_text(size = 16)
  )

# Mostrar gráfico
print(grafico_categorias)

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/decisiones_delegadas_limpio.jpg",
  plot = grafico_categorias,
  width = 10,      
  height = 6,     
  dpi = 450,        
  device = "jpeg"   
)

############## Gráficos D + E

# Codificar como factores ordenados
datos$pregunta_19 <- factor(datos$pregunta_19, levels = c(
  "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
), ordered = TRUE)

datos$pregunta_20 <- factor(datos$pregunta_20, levels = c(
  "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
), ordered = TRUE)

# Calcular frecuencias
frecuencias_p19 <- datos %>%
  count(pregunta_19)

# Distribución de respuestas a la pregunta 19
g_pregunta_19 <- ggplot(frecuencias_p19, aes(x = pregunta_19, y = n)) +
  geom_col(fill = "#4b95d2") +
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
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_19.jpg",
  plot = g_pregunta_19,
  width = 10,      
  height = 5.8,     
  dpi = 400,        
  device = "jpeg"   
)

# Calcular frecuencias
frecuencias_p20 <- datos %>%
  count(pregunta_20)

# Crear gráfico con etiquetas
g_pregunta_20 <- ggplot(frecuencias_p20, aes(x = pregunta_20, y = n)) +
  geom_col(fill = "#fc8d62") +
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

# Guardar
ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_20.jpg",
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


# Gráfica F
grafico_p5 <- datos %>% 
  count(pregunta_5, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_5, -porcentaje), y = porcentaje, fill = pregunta_5)) +
  geom_col() +
  labs(
    title = "Sesgos en la IA en la toma de decisiones",
    x = "Respuesta",
    y = "Porcentaje",
    fill = "Respuesta"
  ) +
  theme_minimal(base_size = 16) +
  theme(
    axis.text.x = element_blank(),
    axis.title.x = element_blank(),
    axis.ticks.x = element_blank(),
    plot.title = element_text(hjust = 0.5, face = "bold")

  )

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/grafica_F_sesgos_IA.jpg",
  plot = grafico_p5,
  width = 8, height = 5, dpi = 350
)


# Pregunta 6: ¿Las personas tienen sesgos?
datos$pregunta_6 <- factor(datos$pregunta_6)

datos$pregunta_6 <- recode(datos$pregunta_6,
"Sí, siempre tenemos algún tipo de sesgo" = "Sí, siempre tenemos\nalgún tipo de sesgo", 
"A menudo, en función del contexto" = "En función del contexto", 
"No, las personas podemos decidir de forma totalmente objetiva" = "No, las personas\npodemos decidir de forma\ntotalmente objetiva"
)

# Gráfica G
grafico_p6 <- datos %>%
  count(pregunta_6, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_6, -porcentaje), y = porcentaje, fill = pregunta_6)) +
  geom_col() +
  labs(
    title = "Sesgos en las personas en la\ntoma de decisiones",
    x = "Respuesta",
    y = "Porcentaje",
    fill = "Respuesta"
  ) +
  theme_minimal(base_size = 16) +
  theme(
    axis.text.x = element_blank(),
    axis.title.x = element_blank(),
    axis.ticks.x = element_blank(),
    plot.title = element_text(hjust = 0.5, face = "bold")
  )

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/grafica_E_sesgos_humanos.jpg",
  plot = grafico_p6,
  width = 8, height = 5, dpi = 350
)


# Comparación gráfica F con pregunta 7 + gráfica G con pregunta 7

datos$pregunta_7 <- factor(datos$pregunta_7)

tabla_p5_p7 <- table(datos$pregunta_5, datos$pregunta_7)
print(tabla_p5_p7)

# Visualizar proporciones por fila
prop.table(tabla_p5_p7, 1)


tabla_p6_p7 <- table(datos$pregunta_6, datos$pregunta_7)
print(tabla_p6_p7)

# Visualizar proporciones por fila
prop.table(tabla_p6_p7, 1)


# Relación entre percepción de sesgo en IA y quién tiene más sesgos
chisq.test(tabla_p5_p7)

# Relación entre percepción de sesgo en humanos y quién tiene más sesgos
fisher.test(tabla_p5_p7)
fisher.test(tabla_p6_p7)


### Gráficas en relacion con la regulación de la IA


datos$pregunta_8 <- factor(datos$pregunta_8)
datos$pregunta_9 <- factor(datos$pregunta_9)

# Crear un vector de colores personalizados
colores_p8 <- c(
  "Las empresas que desarrollan los algoritmos" = "#f47169",  
  "Los gobiernos y organismos reguladores" = "#17a144",
  "Los usuarios, que deben usar la IA de forma crítica" = "#ffee00",
  "Todos los anteriores comparten responsabilidad" = "#66a5f3"
)

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
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/confianza_vs_sesgos.png",
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
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/uso_vs_sesgos.png",
  plot = grafico_uso_vs_sesgos,
  width = 7,
  height = 5,
  dpi = 350
)

# Gráfico: Responsable de evitar sesgos
grafico_p8 <- datos %>%
  count(pregunta_8, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_8, -porcentaje), y = porcentaje, fill = pregunta_8)) +
  geom_col() +
  scale_fill_manual(values = colores_p8) +
  labs(
    title = "¿Quién debería evitar los sesgos en la IA?",
    x = NULL,
    y = "Porcentaje",
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
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/responsable_sesgos_IA.png",
  plot = grafico_p8,
  width = 10,
  height = 5,
  dpi = 350
)

# Crear un vector de colores personalizados
colores_p9 <- c(
  "Los desarrolladores de IA" = "#4b95d2",  # Azul
  "Las autoridades gubernamentales" = "grey70",
  "Los usuarios finales" = "grey70",
  "Organizaciones independientes o de derechos humanos" = "grey70",
  "Otro" = "grey70"
)

# Gráfico: Etapa más importante para educar sobre la IA
grafico_p9 <- datos %>%
  count(pregunta_9, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_9, -porcentaje), y = porcentaje, fill = pregunta_9)) +
  geom_col() +
  scale_fill_manual(values = colores_p9) +
  labs(
    title = "Etapa clave para educar sobre la IA",
    x = NULL,
    y = "Porcentaje",
    fill = "Etapa educativa"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_blank(),
    axis.ticks.x = element_blank(),
    plot.title = element_text(hjust = 0.5, face = "bold")
  )

# Guardar gráfico
ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/educacion_sobre_IA.png",
  plot = grafico_p9,
  width = 10,
  height = 5,
  dpi = 350
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
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/principios.png",
  plot = principios,
  width = 9,
  height = 6,
  dpi = 400
)

# ####################

# # Convertir preguntas éticas a factores ordenados
# datos$pregunta_16 <- factor(datos$pregunta_16, levels = c(
#   "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
# ), ordered = TRUE)

# datos$pregunta_17 <- factor(datos$pregunta_17, levels = c(
#   "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
# ), ordered = TRUE)

# datos$pregunta_18 <- factor(datos$pregunta_18, levels = c(
#   "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
# ), ordered = TRUE)

# # Convertir las preguntas del caso a factores
# datos$pregunta_10 <- factor(datos$pregunta_10)
# datos$pregunta_13 <- factor(datos$pregunta_13)
# datos$pregunta_14 <- factor(datos$pregunta_14)

# colores_eticos <- c(
#   "Totalmente desacuerdo" = "#49006a",
#   "Desacuerdo" = "#4b62a6",
#   "Neutral" = "#2b8cbe",
#   "Acuerdo" = "#66c2a4",
#   "Totalmente acuerdo" = "#ffff33"
# )

# ############### CASO 1
# # Reorganizar en formato largo: Principios vs pregunta_10
# principios_p10 <- datos %>%
#   select(pregunta_10, principio1 = pregunta_16, principio2 = pregunta_17, principio3 = pregunta_18) %>%
#   pivot_longer(cols = starts_with("principio"),
#                names_to = "principio",
#                values_to = "nivel_acuerdo") %>%
#   mutate(
#     principio = recode(principio,
#                        "principio1" = "Dignidad humana",
#                        "principio2" = "Libertad",
#                        "principio3" = "Justicia social"),
#     nivel_acuerdo = factor(nivel_acuerdo, levels = c(
#       "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
#     ), ordered = TRUE)
#   )

# # Gráfico facetado para la pregunta 10
# ggplot(principios_p10, aes(x = pregunta_10, fill = nivel_acuerdo)) +
#   geom_bar(position = "fill") +
#   facet_wrap(~ principio) +
#   scale_fill_manual(values = colores_eticos) +
#   labs(
#     title = "Principios éticos vs ¿Quién tenía razón? (Caso 1)",
#     x = "¿Quién tenía razón?",
#     y = "Proporción",
#     fill = "Nivel de acuerdo con el principio"
#   ) +
#   theme_minimal(base_size = 14) +
#   theme(plot.title = element_text(hjust = 0.5, face = "bold"))

# ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/principios_vs_p10.png", width = 13, height = 7, dpi = 400)


# ############### CASO 2
# principios_p13 <- datos %>%
#   select(pregunta_13, principio1 = pregunta_16, principio2 = pregunta_17, principio3 = pregunta_18) %>%
#   mutate(
#     pregunta_13 = recode(
#       pregunta_13,
#       "El joven estadounidense de 17 años" = "Joven\n17 años",
#       "La empresa desarrolladora de la IA." = "Empresa\ndesarrolladora de\nla app",
#       "El entorno del joven (familiares, escuela, amigos, etc.)" = "Entorno\n del joven"
#     )
#   ) %>%
#   pivot_longer(cols = starts_with("principio"),
#                names_to = "principio",
#                values_to = "nivel_acuerdo") %>%
#   mutate(
#     principio = recode(principio,
#                        "principio1" = "Dignidad humana",
#                        "principio2" = "Libertad",
#                        "principio3" = "Justicia social"),
#     nivel_acuerdo = factor(nivel_acuerdo, levels = c(
#       "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
#     ), ordered = TRUE)
#   )

# ggplot(principios_p13, aes(x = pregunta_13, fill = nivel_acuerdo)) +
#   geom_bar(position = "fill") +
#   facet_wrap(~ principio) +
#   scale_fill_manual(values = colores_eticos) +
#   labs(
#     title = "Principios éticos vs ¿Quién tiene mayor responsabilidad? (Caso 2)",
#     x = "Responsabilidad percibida",
#     y = "Proporción",
#     fill = "Nivel de acuerdo"
#   ) +
#   theme_minimal(base_size = 14) +
#   theme(
#     plot.title = element_text(hjust = 0.5, face = "bold"),
#     axis.text.x = element_text(size = 11)
#   )

# ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/principios_vs_p13.png", width = 13, height = 7, dpi = 350)

# ############### CASO 3
# principios_p14 <- datos %>%
#   select(pregunta_14, principio1 = pregunta_16, principio2 = pregunta_17, principio3 = pregunta_18) %>%
#   mutate(
#     pregunta_14 = recode(
#       pregunta_14,
#       "El hombre que mantenía la conversación" = "Hombre que\nmantenia la\nconversación",
#       "La empresa responsable del chatbot" = "Empresa\nresponsable\ndel chatbot",
#       "La plataforma (Chai) que permitió la interacción" = "Plataforma\nque permitió\nla iterracción"
#     )
#   ) %>%
#   pivot_longer(cols = starts_with("principio"),
#                names_to = "principio",
#                values_to = "nivel_acuerdo") %>%
#   mutate(
#     principio = recode(principio,
#                        "principio1" = "Dignidad humana",
#                        "principio2" = "Libertad",
#                        "principio3" = "Justicia social"),
#     nivel_acuerdo = factor(nivel_acuerdo, levels = c(
#       "Totalmente desacuerdo", "Desacuerdo", "Neutral", "Acuerdo", "Totalmente acuerdo"
#     ), ordered = TRUE)
#   )

# ggplot(principios_p14, aes(x = pregunta_14, fill = nivel_acuerdo)) +
#   geom_bar(position = "fill") +
#   facet_wrap(~ principio) +
#   scale_fill_manual(values = colores_eticos) +
#   labs(
#     title = "Principios éticos vs ¿Quién consideras más responsable? (Caso 3)",
#     x = "Percepción de responsabilidad",
#     y = "Proporción",
#     fill = "Nivel de acuerdo"
#   ) +
#   theme_minimal(base_size = 14) +
#   theme(
#     plot.title = element_text(hjust = 0.5, face = "bold"),
#     axis.text.x = element_text(size = 11)
#   )

# ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/principios_vs_p14.png", width = 13, height = 7, dpi = 350)



##Gráfica etapa más importante para conscienciar sobre la IA
datos$pregunta_9 <- recode(datos$pregunta_9,
  "En la educación primaria y secundaria (colegios)" = "Educación primaria/secundaria",
  "En la universidad" = "Universidad",
  "En el ámbito laboral" = "Ámbito laboral",
  "No creo que sea necesario regular ni concienciar sobre la IA" = "No es necesario concienciar"
)

datos$pregunta_9 <- factor(datos$pregunta_9, levels = c(
  "Educación primaria/secundaria",
  "Universidad",
  "Ámbito laboral",
  "No es necesario concienciar"
))

colores_etapas <- c(
  "Educación primaria/secundaria" = "#ffff33",
  "Universidad" = "#66c2a4",
  "Ámbito laboral" = "#4b62a6",
  "No es necesario concienciar" = "#49006a"
)

frecuencias_p9 <- datos %>%
  count(pregunta_9, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1))


grafico_p9 <- ggplot(frecuencias_p9, aes(x = reorder(pregunta_9, -porcentaje), y = porcentaje, fill = pregunta_9)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +  # 👈 Añade el número de votos encima de cada barra
  scale_fill_manual(values = colores_etapas) +
  labs(
    title = "¿En qué etapa se debería conscienciar y educar\nsobre el uso y los riesgos de la IA?",
    x = NULL,
    y = "Porcentaje",
    fill = "Responsable"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_blank(),       # 👈 Oculta los textos del eje X
    axis.ticks.x = element_blank(),      # 👈 Oculta las marcas del eje X
    plot.title = element_text(hjust = 0.5, face = "bold")
  )

# Guardar gráfico
ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/educacion_IA_etapas.png",
  plot = grafico_p9,
  width = 10,
  height = 6,
  dpi = 350
)
##########################################################################

colores_caso1 <- c(
  "Jake Moffatt" = "#f47169",      
  "La empresa Air Canada" = "#4daf4a"
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

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_10_resultado.png", grafico_p10, width = 10, height = 7, dpi = 440)


################ CASO 2

datos$pregunta_13 <- recode(datos$pregunta_13,
  "El joven estadounidense de 17 años" = "El joven\nestadounidense de\n17 años",
  "La empresa desarrolladora de la IA."= "La empresa\ndesarrolladora\nde la IA",
  "El entorno del joven (familiares, escuela, amigos, etc.)" = "El entorno del joven"
)

grafico_p13 <- datos %>%
  count(pregunta_13, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_13, -porcentaje), y = porcentaje, fill = pregunta_13)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
  labs(
    title = "¿Quién tiene mayor responsabilidad? (Caso 2)",
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

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_13_resultado.png", grafico_p13, width = 10, height = 6, dpi = 350)


################ CASO 3

datos$pregunta_14 <- recode(datos$pregunta_14,
  "El hombre que mantenía la conversación" = "Hombre que\nmantenia la\nconversación",
  "La empresa responsable del chatbot" = "Empresa\nresponsable\ndel chatbot",
  "La plataforma (Chai) que permitió la interacción" = "Plataforma\nque permitió\nla iterracción"
)

grafico_p14 <- datos %>%
  count(pregunta_14, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_14, -porcentaje), y = porcentaje, fill = pregunta_14)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
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

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_14_resultado.png", grafico_p14, width = 10, height = 6, dpi = 350)



datos$pregunta_12 <- recode(datos$pregunta_12,
  "No, deberían estar restringidas por edad" = "No, deberían estar\nrestringidas por edad ",
  "Sí, siempre que el usuario acepte los términos de uso" = "Sí, siempre que el\nusuario acepte los\ntérminos de uso",
  "Deberían estar etiquetadas con advertencias sobre su contenido" = "Deberían estar etiquetadas\ncon advertencias sobre\nsu contenido"
)

grafico_p12 <- datos %>%
  count(pregunta_12, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_12, -porcentaje), y = porcentaje, fill = pregunta_12)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
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

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_12_resultado.png", grafico_p12, width = 12, height = 7, dpi = 400)

datos$pregunta_15 <- recode(datos$pregunta_15,
  "Sí, debería ser un requisito mínimo" = "Sí, debería ser un\nrequisito mínimo", 
  "No, la responsabilidad final siempre debería recaer en el usuario" = "No, la responsabilidad final\nsiempre debería recaer\nen el usuario", 
  "Depende del tipo de IA y su finalidad" = "Depende del tipo de IA\ny su finalidad"
)

grafico_p15 <- datos %>%
  count(pregunta_15, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_15, -porcentaje), y = porcentaje, fill = pregunta_15)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.5, size = 5) +
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

ggsave("C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_15_resultado.png", grafico_p15, width = 12, height = 7, dpi = 400)
