# Instalar paquetes si no los tienes
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

# Filtrar datos: excluir No binario y edades con muy pocos casos
datos_filtrados <- datos %>%
  filter(
    genero != "No binario",
    !(edad %in% c("35 - 44", "Prefiero no decirlo", "Mayor de 64"))
  )

# Invertir niveles de confianza para visualizar desde "Muy alta" hasta "Muy baja"
datos_filtrados$pregunta_23 <- factor(
  datos_filtrados$pregunta_23,
  levels = rev(c("Muy baja", "Baja", "Media", "Alta", "Muy alta")),
  ordered = TRUE
)

# # Paleta personalizada (de azul a rojo según confianza)
# colores_confianza <- c(
#   "Muy alta" = "#4575b4",
#   "Alta"     = "#91bfdb",
#   "Media"    = "#fee090",
#   "Baja"     = "#fc8d59",
#   "Muy baja" = "#d73027"
# )

colores_confianza <- c(
    "Muy baja" = "#49006a",
    "Baja"     = "#2b8cbe",
    "Media"    = "#66c2a4",
    "Alta"     = "#ffff33"
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

# Guardar imagen
ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/confianza_genero.png",
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

# Guardar imagen
ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/confianza_edad.png",
  plot = grafico_edad,
  width = 7,
  height = 5,
  dpi = 300
)


# Convertir uso de IA y edad en factores si no lo son
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


# Guardar gráfico
ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/uso_IA_por_edad.png",
  plot = grafico_uso_edad,
  width = 7,
  height = 5,
  dpi = 300
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
    axis.title = element_text(size = 14),
    axis.text = element_text(size = 14),
    legend.title = element_text(size = 14),
    legend.text = element_text(size = 14)
  )

# Mostrar gráfico
print(grafico_categorias)

ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/decisiones_delegadas_limpio.jpg",
  plot = grafico_categorias,
  width = 10,      
  height = 5,     
  dpi = 350,        
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


# Distribución de respuestas a la pregunta 19
g_pregunta_19 <-ggplot(datos, aes(x = pregunta_19)) +
  geom_bar(fill = "#4b95d2") +
  labs(
    title = "Opinión sobre el impacto actual de la IA",
    x = "Nivel de acuerdo",
    y = "Número de respuestas"
  ) +
  theme_minimal(base_size = 17) +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 14),
    axis.text = element_text(size = 14),
    legend.title = element_text(size = 14),
    legend.text = element_text(size = 14)
  )


ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_19.jpg",
  plot = g_pregunta_19,
  width = 10,      
  height = 5,     
  dpi = 350,        
  device = "jpeg"   
)

# Distribución de respuestas a la pregunta 20
g_pregunta_20 <- ggplot(datos, aes(x = pregunta_20)) +
  geom_bar(fill = "#fc8d62") +
  labs(
    title = "Opinión sobre el impacto futuro de la IA",
    x = "Nivel de acuerdo",
    y = "Número de respuestas"
  ) +
  theme_minimal(base_size = 17) +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    axis.title = element_text(size = 14),
    axis.text = element_text(size = 14),
    legend.title = element_text(size = 14),
    legend.text = element_text(size = 14)
  )


ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_20.jpg",
  plot = g_pregunta_20,
  width = 10,      
  height = 5,     
  dpi = 350,        
  device = "jpeg"   
)

# Tabla cruzada y proporciones
tabla_cruzada <- table(datos$pregunta_19, datos$pregunta_20)
prop.table(tabla_cruzada, 1)  # Por fila

# Tabla cruzada
tabla_cruzada <- table(datos$pregunta_19, datos$pregunta_20)

# Convertir tabla en data frame largo
df_long <- as.data.frame(tabla_cruzada)
colnames(df_long) <- c("P19", "P20", "Frecuencia")

# Crear heatmap con ggplot2
ggplot(df_long, aes(x = P20, y = P19, fill = Frecuencia)) +
  geom_tile(color = "white") +
  scale_fill_gradient(low = "white", high = "#66adc2") +
  labs(
    title = "Relación entre percepción actual y futura de la IA",
    x = "P20: Impacto futuro",
    y = "P19: Impacto actual"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

########################### Gráficos F + E + G : Percepción sobre sesgos en IA y humanos

# Pregunta 5: ¿Crees que la IA toma decisiones sesgadas?
datos$pregunta_5 <- factor(datos$pregunta_5)

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
  width = 12, height = 5, dpi = 350
)


# Pregunta 6: ¿Las personas tienen sesgos?
datos$pregunta_6 <- factor(datos$pregunta_6)

grafico_p6 <- datos %>%
  count(pregunta_6, name = "n") %>%
  mutate(porcentaje = round(n / sum(n) * 100, 1)) %>%
  ggplot(aes(x = reorder(pregunta_6, -porcentaje), y = porcentaje, fill = pregunta_6)) +
  geom_col() +
  labs(
    title = "Sesgos en las personas en la toma de decisiones",
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
  width = 12, height = 5, dpi = 350
)


# Tabla cruzada entre pregunta 5 y 6
tabla_p5_p6 <- table(datos$pregunta_5, datos$pregunta_6)
print(tabla_p5_p6)

# Prueba estadística: Chi-cuadrado
chisq.test(tabla_p5_p6)





# # ANÁLISIS 2: Principios éticos vs uso IA y experiencia
# # Convertir ética a valores numéricos
# etica <- datos %>%
#   mutate(across(c(pregunta_16, pregunta_17, pregunta_18), ~as.numeric(.)))

# # Comparar por uso IA (pregunta_2)
# ggplot(etica, aes(x = pregunta_2, y = as.numeric(pregunta_16))) +
#   geom_boxplot() +
#   labs(title = "Dignidad humana vs Uso de IA", x = "Uso IA", y = "Nivel acuerdo") +
#   theme_minimal()

# kruskal.test(as.numeric(pregunta_16) ~ pregunta_2, data = etica)

# # ANÁLISIS 3: Decisiones delegables (pregunta_21) por conocimiento/confianza
# # Separar respuestas múltiples de pregunta_21
# decision_split <- datos %>%
#   separate_rows(pregunta_21, sep = ",") %>%
#   mutate(pregunta_21 = str_trim(pregunta_21))

# # Gráfico: decisiones más elegidas
# decision_split %>%
#   count(pregunta_21) %>%
#   ggplot(aes(x = reorder(pregunta_21, n), y = n)) +
#   geom_col(fill = "steelblue") +
#   coord_flip() +
#   labs(title = "Tipos de decisiones que se delegarían a una IA", x = "", y = "Frecuencia") +
#   theme_minimal()

# # Relación con conocimiento (pregunta_22)
# ggplot(decision_split, aes(x = pregunta_22, fill = pregunta_21)) +
#   geom_bar(position = "fill") +
#   labs(title = "Tipos de decisiones delegadas por nivel de conocimiento", x = "Conocimiento sobre IA", y = "Proporción") +
#   theme_minimal()





