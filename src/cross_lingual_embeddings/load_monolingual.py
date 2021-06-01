import io
import numpy as np
import codecs
import pickle


def load_embedding(fname, number_tokens=5000):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    words = []
    embedding = []
    for index, line in enumerate(fin):
        if index == 0:
            continue
        tokens = line.rstrip().split(' ')
        words.append(tokens[0].lower())
        embedding.append(tokens[1:])
        if index == number_tokens:
            return words, np.array(embedding).astype("float32")
    return words, np.array(embedding)


def load_translation_dict(dict_path):
    translation_source = []
    translation_target = []
    file_type = dict_path.split(".")[-1]
    if file_type == "tsv":
      for line in list(codecs.open(dict_path, "r", encoding='utf8', errors='replace').readlines()):
          line = line.strip().split("\t")
          translation_source.append(line[0].lower())
          translation_target.append(line[1].lower())
    elif file_type == "txt":
      with open(dict_path) as file_in:
          lines = []
          for line in file_in:
              line = line.rstrip("\n")
              line = ' '.join(line.split())
              [src, trg] = line.split(" ")
              translation_source.append(src.lower())
              translation_target.append(trg.lower())
    else:
        print("No supported dictionary file type")


    return translation_source, translation_target

def save_clew(clew_method, name):
    with open(name + '_src_emb.pkl', 'wb') as f:
        pickle.dump(clew_method.proj_embedding_source_target, f)

    with open(name + '_trg_emb.pkl', 'wb') as f:
        pickle.dump(clew_method.target_embedding_matrix, f)

    with open(name + '_src_word.pkl', 'wb') as f:
        pickle.dump(clew_method.src_word2ind, f)

    with open(name + '_trg_word.pkl', 'wb') as f:
        pickle.dump(clew_method.trg_word2ind, f)
