# Limpiar el entorno
rm(list = ls())

# Cargar datos
data <- read.csv("C:/Users/isall/OneDrive/UNI/TFG/TFG/datos.csv", sep = ",", stringsAsFactors = FALSE)

# Verifica los nombres de las columnas
print(names(data))

# Limpieza y transformación: convertir a texto, eliminar espacios, pasar a minúsculas
for (col in c("pregunta_18", "pregunta_19", "pregunta_20")) {
  data[[col]] <- tolower(trimws(as.character(data[[col]])))
}

# Mapeo de respuestas Likert (en minúsculas para que coincida con la limpieza)
likert_map <- c(
  "totalmente desacuerdo" = 1,
  "desacuerdo"             = 2,
  "neutral"                = 3,
  "acuerdo"                = 4,
  "totalmente acuerdo"     = 5
)

# Aplicar el mapeo a las columnas
data$pregunta_18_num <- likert_map[data$pregunta_18]
data$pregunta_19_num <- likert_map[data$pregunta_19]
data$pregunta_20_num <- likert_map[data$pregunta_20]

# Comprobación: ¿hay respuestas no convertidas (NA)?
cat("NAs en cada pregunta:\n")
cat("P18:", sum(is.na(data$pregunta_18_num)), "\n")
cat("P19:", sum(is.na(data$pregunta_19_num)), "\n")
cat("P20:", sum(is.na(data$pregunta_20_num)), "\n")

# Test de Wilcoxon por pares (solo funciona con pares)
res_18_19 <- wilcox.test(data$pregunta_18_num, data$pregunta_19_num, paired = TRUE)
res_18_20 <- wilcox.test(data$pregunta_18_num, data$pregunta_20_num, paired = TRUE)
res_19_20 <- wilcox.test(data$pregunta_19_num, data$pregunta_20_num, paired = TRUE)

# Mostrar resultados
cat("\nResultado 18 vs 19:\n"); print(res_18_19)
cat("\nResultado 18 vs 20:\n"); print(res_18_20)
cat("\nResultado 19 vs 20:\n"); print(res_19_20)

# Gráfico comparativo
boxplot(data$pregunta_18_num, data$pregunta_19_num, data$pregunta_20_num,
        names = c("Principio 1", "Principio 2", "Principio 3"),
        col = c("lightblue", "lightgreen", "lightcoral"),
        main = "Comparación de respuestas (Likert)",
        ylab = "Nivel de acuerdo (1-5)")



