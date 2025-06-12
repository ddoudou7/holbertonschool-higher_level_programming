# 0. Basics of HTTP / HTTPS

## Différences clés

| Aspect | HTTP | HTTPS |
| ------ | ---- | ----- |
| Chiffrement | ❌ Aucun | ✅ SSL/TLS (port 443) |
| Intégrité & Authenticité | Faible | Forte (certificat X.509) |
| Risque MITM | Élevé | Réduit |
| Usage typique | Sites statiques ou tests locaux | Banque, login, API prod |

---

## Anatomie d’une requête / réponse

**Requête GET**


```
GET /api/users?page=2 HTTP/1.1
Host: api.example.com
User-Agent: curl/8.8.0
Accept: application/json
```
# ⬇️  COPIE-COLLE TOUT, SANS RIEN OUBLIER
cat <<'EOF' >> 0-basics_http_https.md
GET /api/users?page=2 HTTP/1.1
Host: api.example.com
User-Agent: curl/8.8.0
Accept: application/json

markdown
Copier
Modifier

**Réponse 200**

HTTP/1.1 200 OK
Content-Type: application/json
...
{ "page": 2, "users": [...] }

yaml
Copier
Modifier

---

## Méthodes HTTP courantes

| Méthode | Rôle | Exemple |
| ------- | ---- | ------- |
| **GET** | Lire | `GET /posts/42` |
| **POST** | Créer | `POST /posts` |
| **PUT**  | Remplacer | `PUT /posts/42` |
| **PATCH**| Modifier partiellement | `PATCH /posts/42` |
| **DELETE**| Supprimer | `DELETE /posts/42` |

---

## Codes-statut incontournables

| Code | Signification | Scénario |
| ---- | ------------- | -------- |
| **200** | OK | Lecture réussie |
| **201** | Created | Ressource créée |
| **301** | Moved Permanently | Redirection HTTP→HTTPS |
| **400** | Bad Request | JSON mal formé |
| **401** | Unauthorized | Token manquant |
| **404** | Not Found | Ressource absente |
| **500** | Internal Server Error | Exception serveur |
\`\`\`
GET /api/users?page=2 HTTP/1.1
Host: api.example.com
User-Agent: curl/8.8.0
Accept: application/json
\`\`\`

**Réponse 200**

\`\`\`
HTTP/1.1 200 OK
Content-Type: application/json
...
{ "page": 2, "users": [...] }
\`\`\`

---

## Méthodes HTTP courantes

| Méthode | Rôle | Exemple |
| ------- | ---- | ------- |
| **GET** | Lire | \`GET /posts/42\` |
| **POST** | Créer | \`POST /posts\` |
| **PUT**  | Remplacer | \`PUT /posts/42\` |
| **PATCH**| Modifier partiellement | \`PATCH /posts/42\` |
| **DELETE**| Supprimer | \`DELETE /posts/42\` |

---

## Codes-statut incontournables

| Code | Signification | Scénario |
| ---- | ------------- | -------- |
| **200** | OK | Lecture réussie |
| **201** | Created | Ressource créée |
| **301** | Moved Permanently | Redirection HTTP→HTTPS |
| **400** | Bad Request | JSON mal formé |
| **401** | Unauthorized | Token manquant |
| **404** | Not Found | Ressource absente |
| **500** | Internal Server Error | Exception serveur |
