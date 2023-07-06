SELECT
  u.name,
  u.email,
  r.description AS role,
  c.description AS claim
FROM
  users u
  JOIN roles r ON u.role_id = r.id
  LEFT JOIN user_claims uc ON u.id = uc.user_id
  LEFT JOIN claims c ON uc.claim_id = c.id
WHERE
  u.id = _INFORMAR_ID_DO_USUARIO_AQUI_;
