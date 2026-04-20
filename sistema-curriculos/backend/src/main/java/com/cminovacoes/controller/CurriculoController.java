package com.cminovacoes.controller;

import com.cminovacoes.model.Curriculo;
import com.cminovacoes.repository.CurriculoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

// Ajuste de CORS para aceitar todas as origens, headers e métodos necessários na nuvem
@CrossOrigin(origins = "*", allowedHeaders = "*", methods = {RequestMethod.GET, RequestMethod.POST, RequestMethod.OPTIONS})
@RestController
@RequestMapping("/candidatos")
public class CurriculoController {

    @Autowired
    private CurriculoRepository repository;

    // Método para salvar o currículo que vem do formulário
    @PostMapping
    public Curriculo cadastrar(@RequestBody Curriculo novoCurriculo) {
        return repository.save(novoCurriculo);
    }

    // Método para listar os candidatos na página do recrutador
    @GetMapping
    public List<Curriculo> listarTodos() {
        return repository.findAll();
    }
}