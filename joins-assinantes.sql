SELECT a.nm_assinante, e.ds_endereco, t.n_fone FROM Assinante a INNER JOIN Endereco e ON a.cd_assinante = e.cd_assinante INNER JOIN Telefone t ON e.cd_endereco = t.cd_endereco;
SELECT a.nm_assinante, r.ds_ramo FROM Assinante a RIGHT JOIN Ramo_Atividade r ON a.cd_ramo = r.cd_ramo;
SELECT a.nm_assinante FROM Assinante a INNER JOIN Tipo_Assinante ta ON a.cd_tipo = ta.cd_tipo INNER JOIN Endereco e ON a.cd_assinante = e.cd_assinante INNER JOIN Municipio m ON e.cd_municipio = m.cd_municipio WHERE m.ds_municipio = 'Pelotas' AND ta.ds_tipo = 'Residencial';
 SELECT nm_assinante FROM Assinante WHERE cd_assinante = (SELECT cd_assinante FROM Telefone HAVING count(*) > 1);
CREATE VIEW vw_relatorio_comercial AS SELECT a.nm_assinante, t.n_fone FROM Assinante a JOIN Telefone t ON a.cd_assinante = t.cd_assinante JOIN Endereco e ON a.cd_assinante = e.cd_assinante JOIN Municipio m ON e.cd_municipio = m.cd_municipio
