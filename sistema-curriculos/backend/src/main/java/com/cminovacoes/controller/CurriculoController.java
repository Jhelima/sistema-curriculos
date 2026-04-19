package com.cminovacoes.controller;

import com.cminovacoes.model.Curriculo;
import com.cminovacoes.repository.CurriculoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@CrossOrigin(origins = "*") // Permite que o Frontend acesse os dados
@RestController
@RequestMapping("/curriculos")
public class CurriculoController {

    @Autowired
    private CurriculoRepository repository;

    @PostMapping
    public Curriculo cadastrar(@RequestBody Curriculo novoCurriculo) {
        return repository.save(novoCurriculo);
    }

    @GetMapping
    public List<Curriculo> listarTodos() {
        return repository.findAll();
    }
}