#!/usr/bin/env bash
# Crea labels, milestones (1 por Sprint/incremento) y Epics (1 por módulo de la EDT).
# Requiere GitHub CLI autenticado:  gh auth login
# Uso:  ./scripts/bootstrap_github.sh <owner>/sgbm
# Editar FECHAS_SPRINT antes de correr (formato AAAA-MM-DD, fecha de la Reunión de Monitoreo y Control).
set -euo pipefail

REPO="${1:?Uso: $0 <owner>/<repo>}"

MODULOS=("Facultad" "Materia" "Libro" "Bibliografia")
FECHAS_SPRINT=("2026-11-24" "2026-12-01" "2026-12-08" "2026-12-15")

echo "── Labels"
crear_label() { gh label create "$1" --repo "$REPO" --color "$2" --description "$3" --force; }
crear_label "tipo:historia"   "1f6feb" "Historia de Usuario"
crear_label "tipo:epic"       "8250df" "Paquete de trabajo de la EDT"
crear_label "tipo:bug"        "d73a4a" "Defecto"
crear_label "tipo:cambio"     "fbca04" "Solicitud de cambio"
crear_label "tipo:riesgo"     "b60205" "Riesgo del proyecto"
crear_label "tipo:doc"        "0e8a16" "Documentación"
crear_label "cambio:pendiente" "ededed" "Cambio sin decisión"
crear_label "cambio:aprobado"  "0e8a16" "Cambio aprobado"
crear_label "cambio:rechazado" "5a5a5a" "Cambio rechazado o diferido"
for m in "${MODULOS[@]}"; do
  crear_label "modulo:${m,,}" "c5def5" "Módulo ${m}"
done

echo "── Milestones (Sprints)"
for i in "${!MODULOS[@]}"; do
  n=$((i + 1))
  gh api "repos/$REPO/milestones" -f title="Sprint $n" \
    -f description="Incremento $n: módulo ${MODULOS[$i]}. Cierra en la Reunión de Monitoreo y Control." \
    -f due_on="${FECHAS_SPRINT[$i]}T23:59:00Z" >/dev/null && echo "Sprint $n" || echo "Sprint $n ya existe"
done

echo "── Epics"
for i in "${!MODULOS[@]}"; do
  n=$((i + 1)); m="${MODULOS[$i]}"
  gh issue create --repo "$REPO" --title "EPIC: Módulo $n — $m" \
    --label "tipo:epic" --label "modulo:${m,,}" --milestone "Sprint $n" \
    --body "Paquete de trabajo de la EDT (Acta, sección III). Las HU de este módulo se vinculan aquí."
done

echo "Listo. Crear el tablero en la pestaña Projects (plantilla 'Board': Backlog / Sprint / En curso / En revisión / Hecho)."
