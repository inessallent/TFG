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

# Gráfico: Frecuencia de uso de IA según la edad
grafico_uso_edad <- ggplot(datos_uso_filtrado, aes(x = edad, fill = pregunta_2)) +
  geom_bar(position = "fill") +
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
















# ANÁLISIS 2: Principios éticos vs uso IA y experiencia
# Convertir ética a valores numéricos
etica <- datos %>%
  mutate(across(c(pregunta_16, pregunta_17, pregunta_18), ~as.numeric(.)))

# Comparar por uso IA (pregunta_2)
ggplot(etica, aes(x = pregunta_2, y = as.numeric(pregunta_16))) +
  geom_boxplot() +
  labs(title = "Dignidad humana vs Uso de IA", x = "Uso IA", y = "Nivel acuerdo") +
  theme_minimal()

kruskal.test(as.numeric(pregunta_16) ~ pregunta_2, data = etica)

# ANÁLISIS 3: Decisiones delegables (pregunta_21) por conocimiento/confianza
# Separar respuestas múltiples de pregunta_21
decision_split <- datos %>%
  separate_rows(pregunta_21, sep = ",") %>%
  mutate(pregunta_21 = str_trim(pregunta_21))

# Gráfico: decisiones más elegidas
decision_split %>%
  count(pregunta_21) %>%
  ggplot(aes(x = reorder(pregunta_21, n), y = n)) +
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(title = "Tipos de decisiones que se delegarían a una IA", x = "", y = "Frecuencia") +
  theme_minimal()

# Relación con conocimiento (pregunta_22)
ggplot(decision_split, aes(x = pregunta_22, fill = pregunta_21)) +
  geom_bar(position = "fill") +
  labs(title = "Tipos de decisiones delegadas por nivel de conocimiento", x = "Conocimiento sobre IA", y = "Proporción") +
  theme_minimal()


