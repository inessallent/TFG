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
    axis.title = element_text(size = 14),
    axis.text = element_text(size = 14),
    legend.title = element_text(size = 14),
    legend.text = element_text(size = 14)
  )


ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_19.jpg",
  plot = g_pregunta_19,
  width = 10,      
  height = 6,     
  dpi = 350,        
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
    axis.title = element_text(size = 14),
    axis.text = element_text(size = 14)
  )

# Guardar
ggsave(
  filename = "C:/Users/isall/OneDrive/UNI/TFG/TFG/pregunta_20.jpg",
  plot = g_pregunta_20,
  width = 10,
  height = 6,
  dpi = 350,
  device = "jpeg"
)


########################### Gráficos F + E + G : Percepción sobre sesgos en IA y humanos

# Pregunta 5: ¿Crees que la IA toma decisiones sesgadas?
datos$pregunta_5 <- factor(datos$pregunta_5)

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
  width = 12, height = 5, dpi = 350
)


# Pregunta 6: ¿Las personas tienen sesgos?
datos$pregunta_6 <- factor(datos$pregunta_6)

# Gráfica G
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
    "Media"     = "#2ddf86", 
    "Alta" = "#ffff33"
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
  width = 7,
  height = 5,
  dpi = 300
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
  dpi = 300
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


